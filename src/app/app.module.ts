import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { LoadScreenComponent } from './components/load-screen/load-screen.component';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { FlexLayoutModule } from '@angular/flex-layout';

import { provideFirebaseApp, initializeApp } from '@angular/fire/app';
import { firebaseConfig } from '../main';
import { getDatabase, provideDatabase } from '@angular/fire/database';
import { getAuth, provideAuth } from '@angular/fire/auth';
import { AngularFireModule } from '@angular/fire/compat';

import { MatButtonModule } from '@angular/material/button';
import { MatCardModule } from '@angular/material/card';
import { MatIconModule } from '@angular/material/icon';
import { MatDialogModule } from '@angular/material/dialog';
import { MatProgressSpinnerModule } from '@angular/material/progress-spinner';
import { environment } from 'src/environments/environment';

@NgModule({
  declarations: [AppComponent, LoadScreenComponent],
  imports: [
    BrowserModule,
    AppRoutingModule,
    BrowserAnimationsModule,
    MatButtonModule,
    MatCardModule,
    FlexLayoutModule,
    MatIconModule,
    MatDialogModule,
    MatProgressSpinnerModule,
    provideFirebaseApp(() => initializeApp(firebaseConfig)),
    provideDatabase(() => getDatabase()),
    provideAuth(() => getAuth()),
    AngularFireModule.initializeApp(environment.firebase),
  ],
  providers: [],
  bootstrap: [AppComponent],
})
export class AppModule {}
