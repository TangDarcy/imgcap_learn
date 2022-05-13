<template>
  <div>
    用户名:<input type="text" v-model="userName" placeholder="请输入用户名" />
    <br /><br />
    密码:<input type="password" v-model="password" placeholder="请输入密码" />
    <br /><br />
    <button @click="login()">登录</button>
    <br /><br />

    <router-link to="/Register">
      <span style="text-align: center; font-size: 14px">账号注册</span>
    </router-link>

    <router-link to="/ChangePwd">
      <span style="text-align: center; font-size: 14px; color: red"
        >修改密码</span
      >
    </router-link>
  </div>
</template>

<script>
import Cookies from "js-cookie";

export default {
  name: "LoginUser",
  data() {
    return {
      userName: "",
      password: "",
    };
  },
  created() {},
  methods: {
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
