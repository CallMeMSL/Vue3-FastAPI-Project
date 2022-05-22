<template>
  <q-layout view="lHh Lpr lFf">

    <q-header bordered  id="siteHeader">

      <q-tabs align="left">
        <a class="q-mx-md"> Material Word Embeddings </a>
        <q-separator vertical inset color="white"/>
        <q-route-tab to="/" label="Main"/>
        <q-route-tab to="/andere" label="Nochwas"/>
        <q-route-tab to="/about" label="Und nochwas"/>

      </q-tabs>
    </q-header>


    <q-page-container>
      <router-view/>
    </q-page-container>
  </q-layout>
</template>

<script lang="ts">
</script>
