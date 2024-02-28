import { enableProdMode } from '@angular/core';
import { platformBrowserDynamic } from '@angular/platform-browser-dynamic';

import { AppModule } from './app/app.module';
import { environment } from './environments/environment';

if (environment.production) {
  enableProdMode();
}

export const firebaseConfig = {
  apiKey: "AIzaSyAUVkAhNCBmKf0KQYiKf_Ow7eN5kDc8ZKA",
  authDomain: "plantdiseasedetection-83796.firebaseapp.com",
  databaseURL: "https://plantdiseasedetection-83796-default-rtdb.firebaseio.com",
  projectId: "plantdiseasedetection-83796",
  storageBucket: "plantdiseasedetection-83796.appspot.com",
  messagingSenderId: "276736650865",
  appId: "1:276736650865:web:92faee319c78b7a35df5d0"
};

platformBrowserDynamic().bootstrapModule(AppModule)
  .catch(err => console.error(err));
