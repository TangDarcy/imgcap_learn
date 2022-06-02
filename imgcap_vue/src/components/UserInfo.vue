<template>
  <div class="userinfo">
    <span class="userinfo_title">个人中心</span>
    <el-form ref="editFormRef" :model="userInfoForm" label-width="70px">
      <el-form-item label="用户名" prop="userName">
        <el-input v-model="userInfoForm.userName" disabled></el-input>
      </el-form-item>
      <el-form-item label="年龄" prop="age">
        <el-input v-model="userInfoForm.age" disabled></el-input>
      </el-form-item>
      <el-form-item label="性别" prop="sex">
        <el-input v-model="userInfoForm.sex" disabled></el-input>
      </el-form-item>
      <el-form-item label="邮箱" prop="email">
        <el-input v-model="userInfoForm.email" disabled></el-input>
      </el-form-item>
      <el-form-item label="手机号" prop="telephone">
        <el-input v-model="userInfoForm.telephone" disabled></el-input>
      </el-form-item>
    </el-form>
  </div>
  <div class="buttonInfo">
    <el-button type="info" plain @click="clkicChangInfo()"
      >修改个人信息</el-button
    >
  </div>
  <div class="buttomPwd">
    <el-button type="info" plain @click="clkicChangePwd()">修改密码</el-button>
  </div>
</template>
<script>
import axios from "axios";
export default {
  data() {
    return {
      param: {
        userName: "",
      },
      userInfoForm: [],
    };
  },
  created() {
    this.getUserInfo();
  },
  methods: {
    getUserInfo() {
      const that = this;
      that.param.userName = sessionStorage.getItem("accessToken");
      console.log(that.param.userName);
      axios
        .post("http://127.0.0.1:5000/getUserInfo", this.param)
        .then(function (response) {
          if (response.data.code == 0) {
            console.log(response.data.user_info);
            that.userInfoForm = response.data.user_info;
          } else if (response.data.code == 1002) {
            console.log("用户名不存在");
          } else {
            console.log("获取数据不成功");
          }
        })
        .catch(function (error) {
          console.log(error);
        });
    },
    clkicChangInfo() {
      this.$router.push({ path: "/changeUserInfo" });
    },
    clkicChangePwd() {
      this.$router.push({ path: "/changePwd" });
    },
  },
};
</script>
<style scoped>
.userinfo {
  padding: 20px 40px 20px 10px;
}
span.userinfo_title {
  display: block;
  width: 100px;
  height: 30px;
  position: relative;
  top: -15px;
  text-align: center;
  background: white;
}
.el-input.is-disabled /deep/ .el-input__inner {
  color: #606266;
  background: whitesmoke;
}
.buttonInfo {
  float: left;
  position: left;
  height: 15px;
  padding-left: 50px;
}
.buttonPwd {
  float: right;
  position: right;
  height: 15px;
}
</style>
