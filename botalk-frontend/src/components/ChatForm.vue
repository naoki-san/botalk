<template>
  <div>
    <div class="history">
      <ul>
        <li v-for="message in messages" :key="message.timestamp">
          {{ message.body }}
          <a :href="message.translationLink" target="_blank">Translate</a> 
          <button @click="speech(message.body)">Voice</button>
          name: {{ message.name }}
        </li>
      </ul>
    </div>
    <div class="input">
      <input v-model="message" @keyup.enter="sendTextMessage"/>
      <button @click="sendTextMessage">Send</button>
      <button @click="startVoiceInput">Voice</button>
    </div>
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
    speech: function(message) {
      const synth = window.speechSynthesis;
      const utterThis = new SpeechSynthesisUtterance(message);
      utterThis.lang = "en-US";
      utterThis.voice = synth.getVoices().find(v => v.lang === "en-US");
      synth.speak(utterThis);
    },
    pushMessage: function(name, body) {
      this.messages.push({
        name,
        body,
        translationLink: `https://www.deepl.com/translator#en/ja/${encodeURIComponent(body)}`,
        timestamp: Date.now()
      });
      setTimeout(() => {
        const container = this.$el.querySelector(".history");
        container.scrollTop = container.scrollHeight;
      }, 0);
    },
    sendMessage: async function(message) {
      this.pushMessage("Me", message);
      const data = { message };
      const response = await fetch("http://localhost:5000/message", {
        method: "POST",
        headers: {
          "Content-Type": "application/json; charset=utf-8"
        },
        body: JSON.stringify(data)
      });
      const json = await response.json();

      this.speech(json.message);

      this.pushMessage("Bot", json.message);
    },
    sendTextMessage: function() {
      this.sendMessage(this.message);
      this.message = "";
    },
    startVoiceInput: function() {
      const recognition = new window.webkitSpeechRecognition();
      recognition.lang = "en-US";
      recognition.onresult = event => {
        const message = event.results[0][0].transcript;
        this.sendMessage(message);
      };
      recognition.start();
    },
  }
};
</script>

<style scoped>
  .history {
    height: 100vh;
    padding-bottom: 30px;
    overflow: scroll;
    
  }
  .input {
    background-color: #e6e6e6;
    width: 100%;
    padding: 16px;
    position: fixed;
    top: auto;
    bottom: 0;
  }
</style>
