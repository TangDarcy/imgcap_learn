<template>
  <div class="changePwd">
    <span class="changePwd_title">修改密码</span>
    <el-form :model="pwdForm" :rules="pwdRules" style="width: 90%">
      <el-form-item label="用户名" prop="userName">
        <el-input v-model="pwdForm.userName" disabled></el-input>
      </el-form-item>
      <el-form-item label="旧密码" prop="oldPwd">
        <el-input v-model="pwdForm.oldPwd" placeholder="填写旧密码"></el-input>
      </el-form-item>
      <el-form-item label="新密码" prop="newPwd1">
        <el-input v-model="pwdForm.newPwd1" placeholder="填写新密码"></el-input>
      </el-form-item>
      <el-form-item label="确认密码" prop="newPwd2">
        <el-input
          v-model="pwdForm.newPwd2"
          placeholder="再次填写新密码"
        ></el-input>
      </el-form-item>
    </el-form>
  </div>
  <div>
    <el-button type="info" plain style="width: 76%" @click="clickChangePwd"
      >提交</el-button
    >
  </div>
</template>
<script>
import axios from "axios";
export default {
  data() {
    return {
      pwdForm: {
        userName: "",
        oldPwd: "",
        newPwd1: "",
        newPwd2: "",
      },
      pwdRules: {
        oldPwd: [
          { required: true, message: "旧密码不能为空", trigger: "blur" },
        ],
        newPwd1: [
          { required: true, message: "新密码不能为空", trigger: "blur" },
        ],
        newPwd2: [
          { required: true, message: "请再次填写新密码", trigger: "blur" },
        ],
      },
    };
  },
  created() {
    this.getUserName();
  },
  methods: {
    getUserName() {
      const that = this;
      that.pwdForm.userName = sessionStorage.getItem("accessToken");
      console.log(that.pwdForm.userName);
    },
    clickChangePwd() {
      const that = this;
      axios
        .post("http://127.0.0.1:5000/changePwd", this.pwdForm)
        .then(function (response) {
          if (response.data.code == 0) {
            console.log("修改成功");
            that.$router.push({ path: "/" });
          } else if (response.data.code == 1006) {
            console.log("用户名不存在");
          } else if (response.data.code == 1007) {
            console.log("新密码输入不同");
          } else if (response.data.code == 1008) {
            console.log("新密码必须与旧密码不同");
          } else if (response.data.code == 1009) {
            console.log("旧密码错误");
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
.changePwd {
  padding: 10px 10px 10px 30px;
}
span.changePwd_title {
  display: block;
  width: 100px;
  height: 30px;
  position: relative;
  top: -15px;
  text-align: left;
  background: white;
}
.el-input.is-disabled /deep/ .el-input__inner {
  color: #606266;
  background: whitesmoke;
}
</style>
