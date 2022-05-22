<template>
  <q-page class="row items-center justify-evenly">
    Python Version im Backend:

    <p>{{platformText}}</p>
  </q-page>
</template>

<script setup lang="ts">
import {api} from 'boot/axios';
import {onMounted, ref} from 'vue';

const platformText = ref<string>('')

function getPlatform() {
  api.get('platform')
    .then((resp) => platformText.value = resp.data)
    .catch((err) => console.log(err))
}

onMounted(() => getPlatform())
</script>
