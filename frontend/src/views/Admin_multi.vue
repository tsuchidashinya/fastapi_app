<template>
    <div>
        <header>
            <div class="header-title">ログイン画面</div>
        </header>
        <main>
            <div class="main-user">ユーザー名<input class="user-input"></div>
            <div class="main-password">パスワード<input class="password-input" id="tsuchida_id"></div>
            <div class="submit1"><input class="login" type="submit" value="ログイン" @click="home"></div>
            <div class="submit"><input class="login" type="submit" value="新規登録"></div>
        </main>
        <footer>
          <!-- <router-link :to="{ name: 'home', params: { prop1: 'huge11', tsuchida: 'tsuchida'} }" >fdffdfd</router-link> -->
        </footer>
        
    </div>
</template>

<script>
export default {
  methods: {
    home() {
      this.$router.push({ name: 'home', params: {tsuchida: document.getElementById("tsuchida_id").value}})
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
