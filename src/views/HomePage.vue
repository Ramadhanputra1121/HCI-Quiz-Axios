<template>
  <ion-page>
    <ion-header>
      <ion-toolbar>
        <ion-title>Tab 1</ion-title>
      </ion-toolbar>
    </ion-header>
    <ion-content :fullscreen="true">
      <ion-grid>
        <h1>Home</h1>
        <ion-row>
          <ion-col>
            <ion-card>
              <ion-card-header>
                <ion-card-title>Kolam</ion-card-title>
                <ion-card-subtitle>10</ion-card-subtitle>
              </ion-card-header>
            </ion-card>
          </ion-col>
          <ion-col>
            <ion-card>
              <ion-card-header>
                <ion-card-title>Kolam Aktif</ion-card-title>
                <ion-card-subtitle>8</ion-card-subtitle>
              </ion-card-header>
            </ion-card>
          </ion-col>
        </ion-row>
        <ion-row>
          <ion-col>
            <ion-card>
              <ion-card-header>
                <ion-card-title>Ikan Hidup</ion-card-title>
                <ion-card-subtitle>182 Ekor</ion-card-subtitle>
              </ion-card-header>
            </ion-card>
          </ion-col>
          <ion-col>
            <ion-card>
              <ion-card-header>
                <ion-card-title>Ikan Mati</ion-card-title>
                <ion-card-subtitle>89 Ekor</ion-card-subtitle>
              </ion-card-header>
            </ion-card>
          </ion-col>
        </ion-row>
        <ion-row>
          <ion-col>
            <ion-card>
              <ion-card-header>
                <ion-card-title>Panen 2022</ion-card-title>
                <ion-card-subtitle>109 Kg</ion-card-subtitle>
              </ion-card-header>
            </ion-card>
          </ion-col>
          <ion-col>
            <ion-card>
              <ion-card-header>
                <ion-card-title>Total Pakan</ion-card-title>
                <ion-card-subtitle>223 Kg</ion-card-subtitle>
              </ion-card-header>
            </ion-card>
          </ion-col>
        </ion-row>

        <h1>TOTAL BERAT IKAN</h1>

        <ion-row>
          <ion-slides page="true" :options="slideOpts">
            <ion-slide>
              <h1>
                <ion-card>
                  <center>
                    <img alt="Silhouette of mountains"
                      src="https://st2.depositphotos.com/1967477/5333/v/600/depositphotos_53337917-stock-illustration-cartoon-catfish.jpg" />
                  </center>
                  <ion-card-header>
                    <head-title>Lele</head-title>
                    <ion-card-title>
                      <blue>200kg</blue>
                    </ion-card-title>
                  </ion-card-header>
                </ion-card>
              </h1>
            </ion-slide>
            <ion-slide>
              <h1>
                <ion-card>
                  <center>
                    <img alt="Silhouette of mountains"
                      src="https://www.kibrispdr.org/data/864/vector-ikan-nila-0.png" />
                  </center>
                  <ion-card-header>
                    <head-title>Nila Merah</head-title>
                    <ion-card-title>
                      <blue>200kg</blue>
                    </ion-card-title>
                  </ion-card-header>
                </ion-card>
              </h1>
            </ion-slide>
            <ion-slide>
              <h1>
                <ion-card>
                  <center>
                    <img alt="Silhouette of mountains"
                      src="data:image/jpeg;base64,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" />
                  </center>
                  <ion-card-header>
                    <head-title>Mas</head-title>
                    <ion-card-title>
                      <blue>200kg</blue>
                    </ion-card-title>
                  </ion-card-header>
                </ion-card>
              </h1>
            </ion-slide>
            <ion-slide>
              <h1>
                <ion-card>
                  <center>
                    <img alt="Silhouette of mountains"
                      src="https://asset.kompas.com/crops/SWIkgFIidvgdYuhi0NqcUyHo-js=/95x0:1023x619/750x500/data/photo/2020/12/02/5fc76e3264189.jpg" />
                  </center>
                  <ion-card-header>
                    <head-title>Kakap</head-title>
                    <ion-card-title>
                      <blue>200kg</blue>
                    </ion-card-title>
                  </ion-card-header>
                </ion-card>
              </h1>
            </ion-slide>
            <ion-slide>
              <h1>
                <ion-card>
                  <center>
                    <img alt="Silhouette of mountains"
                      src="https://cf.shopee.co.id/file/7972e4b47e4ae9fc5afc9cf7206420e9" />
                  </center>
                  <ion-card-header>
                    <head-title>Kembung</head-title>
                    <ion-card-title>
                      <blue>200kg</blue>
                    </ion-card-title>
                  </ion-card-header>
                </ion-card>
              </h1>
            </ion-slide>
          </ion-slides>
        </ion-row>

        <h1>KUALITAS AIR</h1>

        <ion-row>
          <h1>
            <ion-card>
              <ion-card-header>
                <h2>pH</h2>
                <br>
                <subtitle>Normal <blue>6 Kolam</blue>
                </subtitle><br>
                <subtitle>Abnormal <blue>6 Kolam</blue>
                </subtitle>
              </ion-card-header>
            </ion-card>
          </h1>
          <h1>
            <ion-card>
              <ion-card-header>
                <h2>DO</h2>
                <br>
                <subtitle>Normal <blue> 6 Kolam</blue>
                </subtitle><br>
                <subtitle>Abnormal <blue> 6 Kolam</blue>
                </subtitle>
              </ion-card-header>
            </ion-card>
          </h1>
        </ion-row>
      </ion-grid>
    </ion-content>
  </ion-page>
</template>

<script lang="ts">
import { IonCol, IonGrid, IonRow } from '@ionic/vue';
import { IonPage, IonHeader, IonToolbar, IonTitle, IonContent } from '@ionic/vue';
import { IonCard, IonCardHeader, IonCardSubtitle, IonCardTitle } from '@ionic/vue';
import { IonSlides, IonSlide } from '@ionic/vue';
import { defineComponent } from 'vue';

export default defineComponent({
  name: 'HomePage',
  components: {
    IonCol,
    IonGrid,
    IonRow,
    IonCard,
    IonCardHeader,
    IonCardSubtitle,
    IonCardTitle,
    IonSlides,
    IonSlide,
    IonPage,
    IonHeader,
    IonToolbar,
    IonTitle,
    IonContent
  },
  setup() {
    const slideOpts = {
      slidesPerView: 2,
      spaceBetween: 5,
      speed: 400,
      loop: true,
      centeredSlides: true,
 
    };
    return { slideOpts }
  }
});
</script>

<style scoped>
body {
  font-family: Arial, Helvetica, sans-serif;
  background-color: white;
}

h1 {
  font-size: 20px;
  font-weight: 600;
  margin-left: 10px;
}

ion-card-title {
  font-size: 15px;
  color: black;

}

ion-card-subtitle {
  font-size: 25px;
  font-weight: 600;

  text-transform: capitalize;
  color: black;
}

subtitle {
  font-size: 15px;
  font-weight: 600;

  text-transform: capitalize;
  color: black;
}

ion-card {
  background-color: aliceblue;
  padding: 0;
  margin: 2px;

}

img {
  margin: auto;
  padding: 10px;
  height: 150px;
  width: 200px;
}

h2 {
  font-size: 30px;
  color: black;
  margin: 0;
  font-weight: 600;
}

blue {
  color: #2C96F1;
}

head-title {
  margin-top: 0;
  font-size: 25px;
  color: black;
}

</style>