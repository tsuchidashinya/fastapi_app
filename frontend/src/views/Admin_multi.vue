<template>
    <div>
        <header>
            <div class="header-title">ログイン画面</div>
        </header>
        <main>
            <div class="main-user">ユーザー名<input class="user-input" id="tsuchida_name"></div>
            <div class="main-password">パスワード<input type="password" class="password-input" id="tsuchida_id" @keyup.enter="post_data"></div>
            <div class="message">{{ result }}</div>
            <div class="submit1"><input class="login" type="submit" value="ログイン" @click="post_data"></div>
            
        </main>
        <footer>
          <!-- <router-link :to="{ name: 'home', params: { prop1: 'huge11', tsuchida: 'tsuchida'} }" >fdffdfd</router-link> -->
        </footer>
        
    </div>
</template>

<script>
import axios from "axios";

export default {
  data() {
    return {
      result: "      "
    };
  },

  methods: {
   
    
    home() {
      this.$router.push({ name: 'home', params: {tsuchida: document.getElementById("tsuchida_id").value}})
    },
    post_data() {
      axios
        .post("http://192.168.0.9:8000/data/", {
          username: document.getElementById("tsuchida_name").value,
          password: document.getElementById("tsuchida_id").value
        })
        .then(
          function(response) {
            console.log(response.data.password)
            // this.result=response.data.user;
            if (response.data.user != null && response.data.password != null)
              this.$router.push({ name: 'home', params: {tsuchida: response.data.user}})
            else {
              if (response.data.user == null) {
                this.result = "ユーザーが存在しません！！";
                document.getElementById("tsuchida_name").value = "";
                document.getElementById("tsuchida_id").value = "";
              }
              else if (response.data.password == null) {
                this.result = "パスワードが間違っています！！";
                document.getElementById("tsuchida_id").value = "";
              }
            }
          }.bind(this)
        )
        .catch(
          function(error) {
            console.log(error);
          }.bind(this)
        );

    }
  }
}

</script>

<style>
body {
  font-family: "Avenir Next";
  margin: 0;
  padding: 0;
  background-color: #fff;
}
header {
  background-color: greenyellow;
  height: 60px;
  margin: 0;
  padding-left: 3cm;
  font-size: 40px;
  padding: 10px 10px;
  color: rgb(10, 3, 3);
}

li {
  list-style: none;
  /* 以下の2行を削除してください */
  float: left;
  padding: 33px 20px;
}

.header-title {
  margin: 0;
  color: black;
  padding-left: 10px;
  /* border: medium solid black; */
}

.main-user {

  /* padding-top: 170px; */
  /* padding-left: 40%;
  padding-bottom: 0; */
  text-align: center;
  font-size: 20px;
  color: black;
  /* border: medium solid black; */
}

.user-input {
  margin-left: 20px;
  height: 30px;
}

.main-password {
  text-align: center;
  margin-top: 15px;
  /* border: medium solid black; */
  /* padding-left: 40%; */
  color: black;
  font-size: 20px;
}

.password-input {
  margin-left: 20px;
  height: 30px;
}

.submit1 {
  text-align: center;
  margin-top: 40px;
}

.submit {
 text-align: center;
  margin-top: 25px;;
}

.login {
  height: 50px;
  font-size: 25px;
}

main {
  /* margin-left: 40%; */
  margin-top: 100px;
  /* border: medium solid black; */
}
</style>
