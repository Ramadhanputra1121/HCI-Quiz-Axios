<template>
    <ion-page>
      <ion-tabs>
        <ion-router-outlet></ion-router-outlet>
        <ion-tab-bar slot="bottom">
          <ion-tab-button tab="HomePage" href="/tabs/home">
            <ion-icon src="assets/img/Home.svg"></ion-icon>
          </ion-tab-button>
            
          <ion-tab-button tab="PageSecond" href="/tabs/Page2">
            <ion-icon src="assets/img/Rectangle 58.svg"></ion-icon>
          </ion-tab-button>
          
        </ion-tab-bar>
      </ion-tabs>
    </ion-page>
  </template>
  
  <script lang="ts">
  import { defineComponent } from 'vue';
  import { IonTabBar, IonTabButton, IonTabs, IonIcon, IonPage, IonRouterOutlet } from '@ionic/vue';
  
  export default defineComponent({
    name: 'TabsPage',
    components: {IonTabs, IonTabBar, IonTabButton, IonIcon, IonPage, IonRouterOutlet },
    setup() {
      return {

      }
    }
  });
  </script>
