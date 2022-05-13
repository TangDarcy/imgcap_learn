<template>
  <div class="login">
    <span class="login_title">账号密码登录</span>
    <el-form :model="form" style="width: 90%">
      <el-form-item>
        <el-input placeholder="请输入用户名" v-model="userName" />
      </el-form-item>
      <el-form-item>
        <el-input placeholder="请输入密码" v-model="password" />
      </el-form-item>
    </el-form>
  </div>
  <el-button type="info" plain style="width: 78%" @click="toHome"
    >登录</el-button
  >
  <nav>
    <router-link to="/register">
      <span style="font-size: 14px">新用户注册</span>
    </router-link>
  </nav>
</template>

<script>
import Cookies from "js-cookie";

export default {
  name: "ElementLogin",
  data() {
    return {
      userName: "",
      password: "",
    };
  },
  created() {},
  methods: {
    toHome() {
      this.$router.push("./home");
    },
    login: function () {
      let fd = new FormData();
      fd.append("userName", this.userName);
      fd.append("passwd", this.password);
      // console.log(fd.get("passwd"));

      let config = {
        headers: {
          "Content-Type": "multipart/form-data",
        },
      };

      this.$axios
        .post("user/login", fd, config)
        .then((res) => {
          alert(res.data.msg);
          if (res.data.code === 200) {
            Cookies.set("userName", fd.get("userName"));
            this.$router.push({
              path: "/success",
            });
          }
        })
        .catch((res) => {
          alert(res.data.msg);
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
