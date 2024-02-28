import { Injectable } from '@angular/core';
import { MatDialog, MatDialogConfig } from '@angular/material/dialog';
import { Router } from '@angular/router';
import { LoadScreenComponent } from '../components/load-screen/load-screen.component';

@Injectable({
  providedIn: 'root',
})
export class NotifyService {
  shouldShowProgress = 0;
  constructor(private router: Router, private dialog: MatDialog) {}

  showProgress() {
    this.shouldShowProgress += 1;
    if (this.shouldShowProgress > 0) {
      const dialogConfig = new MatDialogConfig();
      dialogConfig.disableClose = true;
      dialogConfig.width = '10rem';
      dialogConfig.height = '10rem';
      this.dialog.open(LoadScreenComponent, dialogConfig);
    }
  }

  hideProgress() {
    this.shouldShowProgress -= 1;
    if (this.shouldShowProgress < 1) {
      this.dialog.closeAll();
      this.shouldShowProgress = 0;
    }
  }
}
