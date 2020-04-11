<template>
  <div>
    <ul>
      <li v-for="message in messages" :key="message.timestamp">
        {{ message.text }} name: {{ message.name }}
      </li>
    </ul>
    <input v-model="chatText" />
    <button v-on:click="sendMessage">Send</button>
  </div>
</template>

<script>
export default {
  data: function() {
    return {
      chatText: "",
      messages: [],
    };
  },
  methods: {
    sendMessage: function () {
      this.messages.push({
        name: "Me",
        text: this.chatText,
        timestamp: Date.now(),
      });
      this.chatText = "";
    }
  }
};
</script>

<style scoped></style>
