/* eslint-disable */
<template>
  <div id="app">
    <GroupsList />
  </div>
</template>
<script>

import GroupsList from "./components/GroupsList.vue";
export default {
  name: "App",
  components: {
    GroupsList,
  },
};
</script>
<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: #2c3e50;
  margin-top: 30px;
}
</style>