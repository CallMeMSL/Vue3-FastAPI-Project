<template>
  <div>
    <q-input v-model="text"></q-input>

    <q-btn v-text="text" @click="helloWorld"></q-btn>
  </div>
</template>

<script setup lang="ts">
import {ref} from 'vue';

const text = ref<string>('hier könnte ihre werbung stehen')

function helloWorld() {
  console.log('Hello World!')
}


</script>

<style scoped>

</style>
