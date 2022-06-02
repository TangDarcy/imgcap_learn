<template>
  <div class="register">
    <span class="re_title">新用户注册</span>
    <el-form :model="reg_form" :rules="regRules" style="width: 90%">
      <el-form-item label="用户名" prop="userName">
        <el-input placeholder="字符长度大于3" v-model="reg_form.userName" />
      </el-form-item>
      <el-form-item label="密码" prop="passWord">
        <el-input
          placeholder="长度大于6且必须包含字母和数字"
          v-model="reg_form.passWord"
        />
      </el-form-item>
      <el-form-item label="年龄" prop="age">
        <el-input placeholder="数字" v-model="reg_form.age" />
      </el-form-item>
      <el-form-item label="性别" prop="sex">
        <el-select v-model="reg_form.sex" placeholder="请选择性别">
          <el-option label="男" value="man" />
          <el-option label="女" value="woman" />
        </el-select>
      </el-form-item>
      <el-form-item label="邮箱" prop="email">
        <el-input placeholder="邮箱" v-model="reg_form.email" />
      </el-form-item>
      <el-form-item label="手机号" prop="telephone">
        <el-input placeholder="手机号" v-model="reg_form.telephone" />
      </el-form-item>
    </el-form>
  </div>
  <el-button type="info" plain style="width: 80%" @click="clkicReg"
    >提交</el-button
  >
</template>
<script>
import axios from "axios";
export default {
  name: "EleRegister",
  data() {
    return {
      reg_form: {
        userName: "",
        passWord: "",
        age: "",
        sex: "",
        email: "",
        telephone: "",
      },
      regRules: {
        userName: [
          { required: true, message: "用户名不能为空", trigger: "blur" },
        ],
        passWord: [
          { required: true, message: "密码不能为空", trigger: "blur" },
        ],
        age: [{ required: true, message: "年龄不能为空", trigger: "blur" }],
        sex: [{ required: true, message: "必须选择性别", trigger: "blur" }],
        email: [{ required: true, message: "邮箱不能为空", trigger: "blur" }],
        telephone: [
          { required: true, message: "电话不能为空", trigger: "blur" },
        ],
      },
    };
  },
  methods: {
    clkicReg() {
      const that = this;
      axios
        .post("http://127.0.0.1:5000/register", this.reg_form)
        .then(function (response) {
          if (response.data.code == 0) {
            console.log("注册成功");
            that.$router.push({ path: "/" });
          } else if (response.data.code == 1005) {
            console.log("用户名已存在");
          }
        })
        .catch(function (error) {
          console.log(error);
        });
    },
  },
};
</script>
<!-- 添加“scoped”属性以将CSS仅限于此组件 -->
<style scoped>
.register {
  padding: 10px 10px 10px 40px;
}
span.re_title {
  display: block;
  width: 100px;
  height: 30px;
  position: relative;
  top: -15px;
  text-align: left;
  background: white;
}
</style>
