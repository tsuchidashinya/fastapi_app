<template>
  <div class="hello">
    <h1>APIにリクエスト</h1>
    <input type="text" v-model="get_key" />
    <input @click="get_data" type="button" value="GET" />
    <br />
    <input type="text" v-model="get_key1" />
    <!-- <input type="text" v-model="get_key2" /> -->
    <input @click="get_data_tsuchida" type="button" value="GET" />
    <br />
    <input type="text" v-model="post_key" />
    <input type="text" v-model="post_val" />
    <input @click="post_data" type="button" value="POST" />
    <p>{{ result }}</p>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "HelloWorld",
  data() {
    return {
      get_key: "hatagi",
      post_key: "tsuchida",
      post_val: "",
      result: "なにか文字列が浮かび上がります。"
    };
    
  },
  methods: {
    get_data() {
      axios
        .get("http://127.0.0.1:8000/data/", {
          params: {
            key: this.get_key
          }
        })
        .then(
          function(response) {
            this.result = response.data;
            console.log(response);
          }.bind(this)
        )
        .catch(
          function(error) {
            this.result = "GETエラー";
            console.log(error);
          }.bind(this)
        );
    },
    get_data_tsuchida() {
        axios
        .get("http://127.0.0.1:8000/datasaikou/", {
          params: {
            tsuchida: this.get_key1
          }
        })
        .then(
          function(response) {
            this.result = response.data;
            console.log(response);
          }.bind(this)
        )
        .catch(
          function(error) {
            this.result = "GETエラー";
            console.log(error);
          }.bind(this)
        );
    },
    post_data() {
      axios
        .post("http://127.0.0.1:8000/data/", {
          name: this.post_key,
          mean: this.post_val
        })
        .then(
          function(response) {
            this.result = response.data.message;
            console.log(response);
          }.bind(this)
        )
        .catch(
          function(error) {
            this.result = "POSTエラー";
            console.log(error);
          }.bind(this)
        );
    }
  }
};
</script>
