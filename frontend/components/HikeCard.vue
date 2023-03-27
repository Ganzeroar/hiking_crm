<template>
  <div class="card hike-card">
    <div class="card-body">
      <h5 class="card-title">{{ hike.hike_name }}</h5>
      <div class="buttons">
            <b-button type="is-success" expanded>Перейти</b-button>
            <!-- <NuxtLink to="/hike">Home page</NuxtLink> -->
        </div>
    </div>
  </div>
</template>

<script>
export default {
  props: ["hike"]
};
</script>
<style>
.hike-card {
  box-shadow: 0 1rem 1.5rem rgba(11, 0, 0, 0.6);
  width: 300px;
  height: 300px;
  padding: 8px;
  display: block;
  margin-left: auto;
  margin-right: auto;
}
</style>