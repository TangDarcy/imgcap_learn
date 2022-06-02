<template>
  <div class="login">
    <span class="login_title">账号密码登录</span>
    <el-form :model="login_form" :rules="loginRules" style="width: 90%">
      <el-form-item prop="userName">
        <el-input placeholder="请输入用户名" v-model="login_form.userName" />
      </el-form-item>
      <el-form-item prop="passWord">
        <el-input placeholder="请输入密码" v-model="login_form.passWord" />
      </el-form-item>
    </el-form>
  </div>
  <el-button type="info" plain style="width: 78%" @click="clkicLogin()"
    >登录</el-button
  >
  <nav>
    <router-link to="/register">
      <span style="font-size: 14px">新用户注册</span>
    </router-link>
  </nav>
</template>

<script>
// import Cookies from "js-cookie";
// // import api from "../api/api_export";
import axios from "axios";
export default {
  name: "ElementLogin",
  data() {
    return {
      login_form: {
        userName: "",
        passWord: "",
      },
      loginRules: {
        userName: [
          { required: true, message: "用户名不能为空", trigger: "blur" },
        ],
        passWord: [
          { required: true, message: "密码不能为空", trigger: "blur" },
        ],
      },
    };
  },
  methods: {
    clkicLogin() {
      const that = this;
      axios
        .post("http://127.0.0.1:5000", this.login_form)
        .then(function (response) {
          if (response.data.code == 0) {
            sessionStorage.setItem("accessToken", response.data.session);
            that.$router.push({ path: "/home" });
          } else if (response.data.code == 1002) {
            console.log("用户名不存在");
          } else if (response.data.code == 1003) {
            console.log("密码错误");
          }
        })
        .catch(function (error) {
          console.log(error);
        });
    },
  },
};
</script>
<style scoped>
.login {
  padding: 10px 10px 10px 40px;
}
span.login_title {
  display: block;
  width: 100px;
  height: 30px;
  position: relative;
  top: -15px;
  text-align: center;
  background: white;
}
</style>
