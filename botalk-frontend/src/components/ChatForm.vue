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
      messages: []
    };
  },
  methods: {
    sendMessage: async function() {
      const message = this.message;
      this.messages.push({
        name: "Me",
        body: message,
        timestamp: Date.now()
      });

      this.message = "";

      const data = { message };
      const response = await fetch("http://localhost:5000/message", {
        method: "POST",
        headers: {
          "Content-Type": "application/json; charset=utf-8"
        },
        body: JSON.stringify(data)
      });
      const json = await response.json();
      this.messages.push({
        name: "Bot",
        body: json.message,
        timestamp: Date.now()
      });
    }
  }
};
</script>

<style scoped></style>
