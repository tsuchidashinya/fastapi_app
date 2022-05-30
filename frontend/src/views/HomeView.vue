<template>
  <header>
  <div class="header-title">{{tsuchida}}さんの掲示板</div>
  <div class="header-omake">
    <a href="admin1">ログイン</a>
    <a href="register">新規登録</a>
  </div>
</header>
<main>
  <div class="tsuchida">{{tsuchida}}はこれからの時代、どうやって生きていけばいいのか、日々模索している</div>
  <div class="naoki"></div>
  <div class="input-tag">
    <textarea class="text-input">初期値</textarea>
  </div>
  
  <div class="input-tag">
    <div class="button-multi">
      <label for="file_photo" class="file_photo1">
        <img class="image" src="../assets/simple.png">
        <input type="file" id="file_photo" style="display:none;" @click="click">
        
      </label>
      <input type="button" value="送信" class="sousin" >
    </div>
  </div>
  {{result}}
</main>
<footer></footer>
</template>

<script>
import $ from 'jquery'
export default {
  props: {
    tsuchida: {
      type: String,
      require: true
    }
  },
  data() {
    return { result: this.tsuchida + "です。"};
  },
  methods: {
    // post_data() {
    //   axios
    //   .post("http://192.168.0.9:8000/main_data", {
    //     username: this.tsuchida
    //   })
    //   .then(
    //     function(response) {

    //     }
    //   )
    // }
    click() {
      const fileInput = document.getElementById("file_photo")
      
    }
  }
}

</script>

<style>

.input-tag {
  float: left;
  width: 100%;
}

.file_photo1 {
  float: left;
  margin-left: 20%;
  /* border: thin solid grey; */
  height: 34px;
  width: 20;
}
.image {
  /* margin-top: 30px; */
  /* border: thin solid grey; */
  margin-left: 0%;
  height: 34px;
  float: left;
}
.sousin {
  margin-right: 18%;
  /* margin-right: 20%; */
  float: right;
  height: 34px;
  width: 50px;
  border: thin solid grey;
}
.button-multi {
  /* padding-left: 20%; */
  /* padding-right: 20%; */
  height: 35px;
  width: 20.25%;
  border: thin solid grey;
  margin-left: 40%;
  float: left;
}
.text-input {
  height: 100px;
  width: 20%;
  border: thin solid grey;
  border-bottom: 0px none;
  resize: none;
  margin-left: 40%;
  font-size: large;
  float: left;
}
.tsuchida {
  font-size: 30px;
  /* border: medium solid green; */
  width: 50%;
  height: auto;
  margin-left: 25%;
}
body {
  font-family: "Avenir Next";
  margin: 0;
  padding: 0;
  background-color: #fff;
}
header {
    background-color: rgb(238, 93, 57);
    height: 60px;
    margin: 0;
    padding-left: 3cm;
    font-size: 40px;
    padding: 10px 10px;
    color: rgb(10, 3, 3);
}

.header-title {
    margin: 0;
    color: black;
    padding-left: 10px;
    float: left;
    /* border: medium solid black; */
}
.header-omake {
    /* border: medium solid black; */
    float: right;
    margin-top: 10px;
    padding: 0;
}
.header-omake a{
    padding-left:  20px;
    font-size: 30px;
    margin: 0;
    float: left;
    text-decoration: none;
    /* border: medium solid black; */
}


main {
/* margin-left: 40%; */
margin-top: 20px;
/* border: medium solid black; */
}
</style>
