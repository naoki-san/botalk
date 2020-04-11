<template>
  <div id="app">
    <!-- <HelloWorld msg="Welcome to Your Vue.js App"/> -->
    
    <ChatForm />
  </div>
</template>

<script>
// import HelloWorld from './components/HelloWorld.vue'
import ChatForm from "./components/ChatForm.vue";

export default {
  name: "App",
  components: {
    ChatForm,
  },
};
</script>

