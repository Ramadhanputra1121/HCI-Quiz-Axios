<template>
  <ion-page>
    <ion-content>
      <div class="kolam-header" style="margin-inline: 30px;">
        <div class="back-btn">
          <a href="/Tabs/Page2">
            <ion-icon src="assets/img/Vector2.svg" style="margin-top: 12px ;"></ion-icon>
          </a>
        </div>

        <div>
          <h2 style="margin-right: 60px;">Registrasi Kolam</h2>
        </div>
      </div>
    </ion-content>
  </ion-page>
  <div style="margin-top: 100px;">
    <ion-header collapse="condense">
      <ion-toolbar>
        <ion-title size="large">Registration Form</ion-title>
      </ion-toolbar>
    </ion-header>
    <ion-list>
      <ion-item>
        <ion-label position="stacked">Nama Kolam</ion-label>
        <ion-input placeholder="Kolam 1" v-model="namakolam"></ion-input>
      </ion-item>
    </ion-list>
    <ion-list>
      <ion-item>
        <ion-label position="stacked">Lokasi Kolam</ion-label>
        <ion-input placeholder="Blok A" v-model="lokasikolam"></ion-input>
      </ion-item>
    </ion-list>
    <ion-list>
      <ion-item>
        <ion-label position="stacked">Material Kolam</ion-label>
        <ion-select interface="action-sheet" v-model="materialkolam">
          <ion-select-option value="tanah">Tanah</ion-select-option>
          <ion-select-option value="beton">Beton</ion-select-option>
          <ion-select-option value="terpal">Terpal</ion-select-option>
        </ion-select>
      </ion-item>
    </ion-list>
    <ion-list>
      <ion-item>
        <ion-label position="stacked">Bentuk Kolam</ion-label>
        <ion-select interface="action-sheet" v-model="bentukkolam">
          <ion-select-option value="kotak">Kotak</ion-select-option>
          <ion-select-option value="bundar">Bundar</ion-select-option>
        </ion-select>
      </ion-item>
    </ion-list>

    <ion-button expand="block" @click="getFormValues()">Registrasi</ion-button>
  </div>

</template>

<script lang="ts">
import { defineComponent } from 'vue';
import { IonPage, IonHeader, IonToolbar, IonTitle, IonContent, IonButton, IonLabel, IonInput, IonItem, IonList, IonSelect, IonSelectOption } from '@ionic/vue';
import axios from 'axios'

export default defineComponent({
  name: 'RegistrationPage',
  components: { IonHeader, IonToolbar, IonTitle, IonContent, IonPage, IonButton, IonLabel, IonInput, IonItem, IonList, IonSelect, IonSelectOption },
  data() {
    return {
      namakolam: '',
      lokasikolam: '',
      materialkolam: '',
      bentukkolam: '',
    }
  },
  methods: {
    getFormValues() {
      let form
      form = [this.namakolam, this.lokasikolam, this.materialkolam, this.bentukkolam]
      console.log(form)
      console.log(this.namakolam)
      console.log(this.lokasikolam)
      console.log(this.materialkolam)
      console.log(this.bentukkolam)

      var api = "http://jft.web.id/fishapi/api/ponds"

      axios.get(api)
        .then(function (response) {
          console.log(response);
        })
        .catch(function (error) {
          console.log(error);
        })
    }

  }
});
</script>

<style scoped>
body {
  background-color: #1F1D2B;
}

.kolam-header {
  vertical-align: middle;
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin: 15px 10px;
  font-weight: bold;
}

.kolam-header img {
  width: 30px;
}
</style>