<template>
    <div>
        <header>
            <div class="header-title">新規登録</div>
        </header>
        <main>
            <div class="user_line"><div class="main-user-left">ユーザー名</div><div class="main-user-right"><input class="user-input" id="tsuchida_name"></div></div>
            <div class="pass_line"><div class="main-password_left">パスワード</div><div class="main-password_right"><input class="password-input" id="tsuchida_pass"></div></div>
            <div class="pass_line"><div class="main-password_left">パスワード(確認)</div><div class="main-password_right"><input class="password-input" id="tsuchida_pass2"></div></div>
            <div class="message">{{ result }}</div>
            <div class="submit"><input class="login" type="submit" value="新規登録" @click="post_data"></div>
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
    post_data() {
      if (document.getElementById("tsuchida_pass").value != document.getElementById("tsuchida_pass2").value) {
        this.result = "パスワードが一致していません！！";
      }
      else {
        axios
        .post("http://127.0.0.1:8000/new_register/", {
          username: document.getElementById("tsuchida_name").value,
          password: document.getElementById("tsuchida_pass").value
        })
        .then(
          function(response) {
            console.log(response.data.register_success)
            this.result=response.data.register_success;
            if (response.data.register_success == true)
              this.$router.push({ name: 'admin1', params: {tsuchida: response.data.register_success}})
            else {
              this.result = "ユーザーがすでに存在しています！！";
              
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
  background-color: orange;
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

.main-user-left {
  float: left;
  text-align: right;
  font-size: 20px;
  color: black;
  width: 49%;
  /* border: medium solid black; */
}

.main-user-right {
  float: left;
  text-align: left;
  font-size: 20px;
  color: black;
  /* border: medium solid black; */
  width: 49%;
}

.user-input {
  margin-left: 20px;
  height: 30px;
}

.main-password_left {
  text-align: right;
  float: left;
  /* border: medium solid black; */
  color: black;
  font-size: 20px;
  width: 49%;
}

.main-password_right {
  text-align: left;
  float: left;
  /* margin-top: 15px; */
  /* border: medium solid black; */
  /* padding-left: 10%; */
  color: black;
  font-size: 20px;
  width: 49%;
}

.user_line {
  text-align: center;
  margin-top: 15px;
  /* border: medium solid green; */
  /* padding-left: 40%; */
  color: black;
  font-size: 40px;
  height: 50px;
}
.pass_line {
  text-align: center;
  margin-top: 15px;
  /* border: medium solid green; */
  /* padding-left: 40%; */
  color: black;
  font-size: 40px;
  height: 50px;
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
