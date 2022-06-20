<template>
  <div v-if="loading === true">loading</div>
  <div v-else-if="loadingError === true">Failed to fetch data please reload page</div>
  <div v-else>
    <div>View Task</div>
  </div>
</template>

<script setup lang="ts">
import { ref, onBeforeMount } from 'vue';
import { useRoute, useRouter } from 'vue-router';
import { useTaskStore } from '../stores/task-store';

const route = useRoute();
const router = useRouter();
const taskStore = useTaskStore();

const loading = ref(true);
const loadingError = ref(false);

const getData = async () => {
  try {
    loading.value = true;
    taskStore.searchTaskByID(route.params.uuid as string);
  } catch (error) {
    loadingError.value = true;
  } finally {
    loading.value = false;
  }
};

const deleteTask = async (uuid: string) => {
  const res = await taskStore.deleteTask(uuid);
  router.push({ path: `/task/:${uuid}` });
  console.log(res);
};

onBeforeMount(() => {
  getData();
});
</script>

<style scoped></style>
