<template>
  <div>
    <main-header></main-header>

    <div class="container mt-5">
      <section class="main-content">
        <div class="container column is-10">
          <b-field label="Все походы и туры">
            <b-input placeholder="Введите название похода" type="text" />
          </b-field>
        </div>

        <div class="container column is-10">
          <template v-for="(hikesInOneRow, index) in hikesColumns">
            <div :key="index" class="columns">
              <div class="column">
                <div :key="hikesInOneRow[0].id" >
                  <hike-card :hike="hikesInOneRow[0]"></hike-card>
                </div>
              </div>
              <div v-if="hikesInOneRow.length > 1" class="column">
                <div :key="hikesInOneRow[1].id" class="col-lg-3 col-md-4 col-sm-6 mb-4">
                  <hike-card :hike="hikesInOneRow[1]"></hike-card>
                </div>
              </div>
              <div v-if="hikesInOneRow.length > 2" class="column">
                <div :key="hikesInOneRow[2].id" class="col-lg-3 col-md-4 col-sm-6 mb-4">
                  <hike-card :hike="hikesInOneRow[2]"></hike-card>
                </div>
              </div>
            </div>
          </template>
        </div>
      </section>

    </div>

  </div>
</template>

<script>
import HikeCard from '~/components/HikeCard.vue';
import MainHeader from '~/components/MainHeader.vue'

export default {
  name: 'DefaultLayout',
  components: {
    HikeCard, MainHeader
  },
  async asyncData({ $axios, params }) {
    try {
      const hikings = await $axios.$get(`/client/hikings`);
      let numberOfRowsInHikingTable = ''
      if (hikings.length % 3 === 0) {
        numberOfRowsInHikingTable = hikings.length / 3
      } else {
        numberOfRowsInHikingTable = Math.floor(hikings.length / 3) + 1
      }

      const hikesColumns = []
      for (let i = 0; i < numberOfRowsInHikingTable; i++) {
        const hikesInOneRow = []
        hikesInOneRow.push(hikings[i * 3])
        if (typeof hikings[i * 3 + 1] === 'undefined') {
          // pass
        }
        else {
          hikesInOneRow.push(hikings[i * 3 + 1])
        }
        if (typeof hikings[i * 3 + 2] === 'undefined') {
          // pass
        }
        else {
          hikesInOneRow.push(hikings[i * 3 + 2])
        }
        hikesColumns.push(hikesInOneRow)
      }

      return { hikings, hikesColumns };
    } catch (e) {
      return { hikings: [] };
    }
  },
}
</script>
<style scoped>
</style>