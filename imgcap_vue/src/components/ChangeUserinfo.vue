<template>
  <div class="changeInfo">
    <span class="changeInfo_title">修改个人信息</span>
    <el-form
      :model="changeInfoForm"
      :rules="chgRules"
      style="width: 90%"
      label-width="70px"
    >
      <el-form-item label="用户名" prop="userName">
        <el-input v-model="changeInfoForm.userName" disabled></el-input>
      </el-form-item>
      <el-form-item label="年龄" prop="age">
        <el-input placeholder="年龄" v-model="changeInfoForm.age"></el-input>
      </el-form-item>
      <el-form-item label="性别" prop="sex">
        <el-select v-model="changeInfoForm.sex" placeholder="请选择性别">
          <el-option label="男" value="man" />
          <el-option label="女" value="woman" />
        </el-select>
      </el-form-item>
      <el-form-item label="邮箱" prop="email">
        <el-input placeholder="邮箱" v-model="changeInfoForm.email"></el-input>
      </el-form-item>
      <el-form-item label="手机号" prop="telephone">
        <el-input
          placeholder="手机号"
          v-model="changeInfoForm.telephone"
        ></el-input>
      </el-form-item>
    </el-form>
  </div>
  <div class="changeInfo">
    <el-button type="info" plain style="width: 80%" @click="changeInfo()"
      >提交</el-button
    >
  </div>
</template>
<script>
import axios from "axios";
export default {
  data() {
    return {
      changeInfoForm: {
        userName: "",
        age: "",
        sex: "",
        email: "",
        telephone: "",
      },
      chgRules: {
        age: [{ required: true, message: "年龄不能为空", trigger: "blur" }],
        sex: [{ required: true, message: "必须选择性别", trigger: "blur" }],
        email: [{ required: true, message: "邮箱不能为空", trigger: "blur" }],
        telephone: [
          { required: true, message: "电话不能为空", trigger: "blur" },
        ],
      },
    };
  },
  created() {
    this.getUserByName();
  },
  methods: {
    getUserByName() {
      const that = this;
      that.changeInfoForm.userName = sessionStorage.getItem("accessToken");
      console.log(that.changeInfoForm.userName);
      axios
        .post("http://127.0.0.1:5000/getUserInfo", this.changeInfoForm)
        .then(function (response) {
          if (response.data.code == 0) {
            console.log(response.data.user_info);
            that.changeInfoForm = response.data.user_info;
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
    changeInfo() {
      const that = this;
      axios
        .post("http://127.0.0.1:5000/changeInfo", this.changeInfoForm)
        .then(function (response) {
          if (response.data.code == 0) {
            console.log("修改成功");
            that.$router.push({ path: "/userInfo" });
          } else if (response.data.code == 1006) {
            console.log("用户名不存在");
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
.changeInfo {
  padding: 10px 10px 10px 10px;
}
span.changeInfo_title {
  display: block;
  width: 100px;
  height: 30px;
  position: relative;
  top: -15px;
  text-align: right;
  background: white;
}
</style>
