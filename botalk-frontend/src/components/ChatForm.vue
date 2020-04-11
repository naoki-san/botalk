<template>
  <div>
    <input v-model="chatText" />
    <p>Message is: {{ chatText }}</p>
  </div>
</template>

<script>
export default {
  data: function() {
    return {
      chatText: ""
    };
  }
};
</script>

<style scoped></style>
