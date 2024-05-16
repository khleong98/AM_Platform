<template>
  <div>
    <h1>User Details</h1>
    <label for="email">Select Email:</label>
    <select v-model="selectedEmail" @change="getUserDetail">
      <option v-for="email in emailOptions" :key="email" :value="email">{{ email }}</option>
    </select>

    <div v-if="userDetail">
      <h2>User Detail</h2>
      <ul>
        <li v-for="(value, key) in userDetail" :key="key">
          {{ key }}: {{ value }}
        </li>
      </ul>
    </div>
  </div>
</template>

<script>
import axios from 'axios';
import { BASE_API_URL } from './apiEndpoint.js';

export default {
  data() {
    return {
      emailOptions: [],
      selectedEmail: '',
      userDetail: null
    };
  },
  methods: {
    async fetchEmailOptions() {
      try {
        const response = await axios.get(BASE_API_URL + 'email'); // Adjust endpoint accordingly
        this.emailOptions = response.data.email;
      } catch (error) {
        console.error('Error fetching email options:', error);
      }
    },
    async getUserDetail() {
      try {
        const response = await axios.post(BASE_API_URL + 'detail', {
          email: this.selectedEmail
        });
        this.userDetail = response.data.detail;
      } catch (error) {
        console.error('Error fetching user detail:', error);
      }
    }
  },
  mounted() {
    this.fetchEmailOptions();
  }
};
</script>
