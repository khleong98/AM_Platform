<template>
  <div>
    <label for="emailDropdown">Select Email:</label>
    <select id="emailDropdown" v-model="selectedEmail" @change="fetchReferralTree">
      <option v-for="email in emails" :key="email" :value="email">{{ email }}</option>
    </select>

    <div v-if="referralTree">
      <h3>Referral Tree:</h3>
      <pre>{{ formatReferralTree(referralTree) }}</pre>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import axios from 'axios';
import { BASE_API_URL } from './apiEndpoint.js';

const emails = ref([]);
const selectedEmail = ref('');
const referralTree = ref(null);

const fetchEmails = async () => {
  try {
    const response = await axios.get(BASE_API_URL + 'email');
    emails.value = response.data.email;
  } catch (error) {
    console.error('Error fetching emails:', error);
  }
};

const fetchReferralTree = async () => {
  if (!selectedEmail.value) return;

  try {
    const response = await axios.get(BASE_API_URL + 'referral', {
      params: { email: selectedEmail.value },
    });
    referralTree.value = response.data.referral;
  } catch (error) {
    console.error('Error fetching referral tree:', error);
  }
};

const formatReferralTree = (tree, level = 0) => {
  let formattedTree = '';
  for (const [email, subTree] of Object.entries(tree)) {
    formattedTree += `${'>>>> '.repeat(level)}${email}\n`;
    for (const subTreeItem of subTree) {
      formattedTree += formatReferralTree(subTreeItem, level + 1);
    }
  }
  return formattedTree;
};

onMounted(() => {
  fetchEmails();
});
</script>

<style scoped>
pre {
  white-space: pre-wrap;
  font-family: monospace;
  text-align: left;
}
</style>
