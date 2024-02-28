import { Component } from '@angular/core';
import { Auth } from '@angular/fire/auth';
import { AngularFireStorage } from '@angular/fire/compat/storage';
import * as FireDb from '@angular/fire/database';
import { get, getDatabase, onValue, push, ref } from '@angular/fire/database';
import { Observable } from 'rxjs';
import { ImageStatus } from './constants';
import { IPlantModel } from './model';
import { NotifyService } from './service/notify.service';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss'],
})
export class AppComponent {
  inputData: any = null;
  srcResult = '';
  downloadURL: Observable<string> = new Observable();
  plantData: IPlantModel[] = [];
  plantStatuses = ImageStatus;

  constructor(
    private auth: Auth,
    private storage: AngularFireStorage,
    private notify: NotifyService
  ) {
    const db = getDatabase();
    onValue(ref(db, 'plant-images'), () => {
      this.fetchData();
    });
  }

  onFileSelected() {
    this.inputData = document.querySelector('#file');
    if (this.inputData != null) {
      this.notify.showProgress();
      const reader = new FileReader();
      reader.onload = (e: any) => {
        this.srcResult = e.target.result;
        const filePath =
          'plant_image_' +
          new Date().getTime() +
          '_' +
          this.inputData.files[0].name;
        const fileRef = this.storage.ref(filePath);

        const uploadTask = this.storage.upload(filePath, this.srcResult);
        uploadTask.then(
          (res) => {
            this.downloadURL = fileRef.getDownloadURL();
            this.downloadURL.subscribe((url) => {
              if (url) {
                const postRef = FireDb.ref(getDatabase(), 'plant-images/');
                push(postRef, {
                  url: url,
                  time: new Date().getTime(),
                  status: ImageStatus.IN_PROGRESS,
                }).then(
                  (res) => {
                    console.log('Upload complete');
                    this.notify.hideProgress();
                  },
                  (err) => {
                    alert('Failed to upload file');
                    console.log(err);
                    this.notify.hideProgress();
                  }
                );
              } else {
                this.notify.hideProgress();
              }
            });
          },
          (err) => {
            alert('Failed to upload file');
            console.log(err);
            this.notify.hideProgress();
          }
        );
      };

      reader.readAsArrayBuffer(this.inputData.files[0]);
    } else {
      alert('Failed to uploadFile');
      this.notify.hideProgress();
    }
  }

  fetchData() {
    const db = getDatabase();
    this.notify.showProgress();
    get(ref(db, 'plant-images'))
      .then((snap) => {
        this.plantData = [];
        if (snap.exists()) {
          snap.forEach((child) => {
            const val = child.val();

            const id = child.key;
            const url = val['url'];
            const time = val['time'];
            const status = val['status'];

            const plant = val['plant'];
            const disease = val['disease'];

            var plantDetail: IPlantModel = {
              id: id,
              url: url,
              time: time,
              plant: plant,
              disease: disease,
              status: status,
            };
            this.plantData.push(plantDetail);
          });

          this.plantData.reverse();

          this.notify.hideProgress();
        } else {
          this.notify.hideProgress();
        }
      })
      .catch((err) => {
        this.notify.hideProgress();
        alert('Failed to get plant data');
      });
  }
}
