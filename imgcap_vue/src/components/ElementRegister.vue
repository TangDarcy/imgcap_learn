<template>
  <div class="register">
    <span class="re_title">新用户注册</span>
    <el-form :model="form" style="width: 90%">
      <el-form-item label="用户名">
        <el-input placeholder="字符长度大于6" v-model="userName" />
      </el-form-item>
      <el-form-item label="密码">
        <el-input
          placeholder="长度大于6且必须包含字母和数字"
          v-model="password"
        />
      </el-form-item>
      <el-form-item label="性别">
        <el-select v-model="sex" placeholder="请选择性别">
          <el-option label="男" value="man" />
          <el-option label="女" value="woman" />
        </el-select>
      </el-form-item>
      <el-form-item label="邮箱">
        <el-input placeholder="邮箱" v-model="email" />
      </el-form-item>
      <el-form-item label="手机号">
        <el-input placeholder="手机号" v-model="telephone" />
      </el-form-item>
    </el-form>
  </div>
  <el-button type="info" plain style="width: 80%" @click="toLogin"
    >提交</el-button
  >
</template>

<script>
export default {
  name: "EleRegister",
  data() {
    return {
      userName: "",
      password: "",
      sex: "",
      email: "",
      telephone: "",
    };
  },
  created() {},
  methods: {
    toLogin() {
      this.$router.push("./");
    },
    register: function () {
      let fd = new FormData();
      fd.append("userName", this.userName);
      fd.append("passwd", this.password);

      let config = {
        headers: {
          "Content-Type": "multipart/form-data",
        },
      };

      if (this.password === this.password2) {
        this.$axios
          .post("user/register", fd, config)
          .then((res) => {
            alert(res.data.msg);
            if (res.data.code === 200) {
              // 回到登录界面
              this.$router.push({
                path: "/",
              });
            }
          })
          .catch((res) => {
            alert(res.data.msg);
          });
      } else {
        alert("两次输入的密码不同");
      }
    },
  },
};
</script>

<!-- 添加“scoped”属性以将CSS仅限于此组件 -->
<style scoped>
span.re_title {
  display: block;
  width: 100px;
  height: 30px;
  position: relative;
  top: -15px;
  text-align: center;
  background: white;
}
</style>
