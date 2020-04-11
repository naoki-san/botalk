<template>
  <div>
    <ul>
      <li v-for="message in messages" :key="message.timestamp">
        {{ message.body }} name: {{ message.name }}
      </li>
    </ul>
    <input v-model="message" />
    <button v-on:click="sendMessage">Send</button>
  </div>
</template>

<script>
export default {
  data: function() {
    return {
      message: "",
      messages: [],
    };
  },
  methods: {
    sendMessage: function () {
      const message = this.message;
      this.messages.push({
        name: "Me",
        body: message,
        timestamp: Date.now(),
      });
      this.message = "";
      
    }
  }
};
</script>

<style scoped></style>
