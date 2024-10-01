<template>
  <div>
    <h2>Sensor Data</h2>
    <input type="text" v-model="searchQuery" placeholder="Search sensor by name">
    <table class="table table-striped">
      <thead>
        <tr>
          <th @click="sortTable('name')">Sensor Name</th>
          <th @click="sortTable('type')">Sensor Type</th>
          <th @click="sortTable('variant')">Sensor Variant</th>
          <th v-for="metric in metrics" :key="metric.id" @click="sortTable(metric.id)">
            {{ metric.name }} ({{ getSelectedUnit(metric.units) }})
          </th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="sensor in filteredSensors" :key="sensor.id">
          <td>{{ sensor.name || 'Unnamed' }}</td>
          <td>{{ sensor.type }}</td>
          <td>{{ sensor.variant }}</td>
          <td v-for="metric in metrics" :key="metric.id">
            {{ getSensorMetricValue(sensor, metric.id) }}
          </td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      sensors: {},  // Initialize as an object
      metrics: [],
      sensorTypes: {},  // Store sensor types
      searchQuery: '',
      sortKey: '',
      sortAsc: true,
    };
  },
  computed: {
    filteredSensors() {
      if (!Array.isArray(this.sensors)) {
        return []; // Return an empty array if sensors is not an array
      }
      return this.sensors.filter(sensor => {
        return sensor.name ? sensor.name.toLowerCase().includes(this.searchQuery.toLowerCase()) : false; // Handle undefined names
      });
    },
  },
  methods: {
    fetchSensorData() {
      // Assuming the API returns both sensors and sensor_types
      axios.get('http://localhost:8000/api/sensors/')
        .then(response => {
          console.log("API response:", response.data);
          this.sensors = Object.values(response.data.sensors || {}); // Convert to array or fallback to empty array
          this.metrics = response.data.metrics;
          this.sensorTypes = response.data.sensor_types || {}; // Store sensor types

          // Map sensors to include type and variant names
          this.sensors = this.sensors.map(sensor => {

            const sensorTypes = sensor.type;

            const variant = sensor.variant;

            const sensorType = this.sensorTypes[sensor.type];

            sensor.name = '' + sensorType[variant].name

            return {
              ...sensor,
              type: sensorTypes || 'Unknown ', // Add type name
              variant: variant || 'Unknown' // Add variant name
            };
          });
        })
        .catch(error => {
          console.error("Error fetching sensors data:", error);
        });
    },
    getSensorMetricValue(sensor, metricId) {
      return sensor.metrics[metricId] ? sensor.metrics[metricId].v : 'N/A';
    },
    getSelectedUnit(units) {
      return units.find(unit => unit.selected)?.name || 'N/A'; // Handle cases with no selected unit
    },
    sortTable(key) {
      this.sortKey = key;
      this.sortAsc = !this.sortAsc;
      this.sensors.sort((a, b) => {
        let aValue = a.metrics[key]?.v || 0; // Use optional chaining
        let bValue = b.metrics[key]?.v || 0;
        let result = aValue > bValue ? 1 : -1;
        return this.sortAsc ? result : -result;
      });
    },
  },
  mounted() {
    this.fetchSensorData();
  },
};
</script>

<style scoped>
.table {
  width: 100%;
  margin: 20px 0;
}
.table th, .table td {
  padding: 8px 12px;
  text-align: left;
}
</style>
