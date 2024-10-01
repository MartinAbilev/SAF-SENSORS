<template>
  <div id="app">
    <h1>Sensor Data Viewer</h1>
    <SensorTable />
  </div>
</template>

<script>
import SensorTable from './components/SensorTable.vue';

export default {
  name: 'App',
  components: {
    SensorTable,
  },
};
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
