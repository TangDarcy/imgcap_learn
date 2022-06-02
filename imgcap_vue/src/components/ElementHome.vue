<template>
  <div class="button_1">
    <el-button type="info" plain @click="clickUserinfo()">个人中心</el-button>
  </div>
  <div class="button_2">
    <el-button type="info" plain @click="clkicDescription()"
      >图像描述管理</el-button
    >
  </div>
  <div class="up_load">
    <!-- <el-upload
      class="upload-demo"
      drag
      action="https://jsonplaceholder.typicode.com/posts/"
      multiple
    >
      <el-icon class="el-icon--upload"><upload-filled /></el-icon>
      <div class="el-upload__text">拖入图片 或者<em> 点击上传图像</em></div>
      <template #tip>
        <div class="el-upload__tip">支持不大于2M的jpg/png文件</div>
      </template>
    </el-upload> -->
    <img :src="defaultImg" />
  </div>
  <div>
    <el-form :model="selecModel" style="width: 100%" label-width="100px">
      <el-form-item label="模型选择" prop="model">
        <el-select v-model="D_model" placeholder="请选择模型">
          <el-option label="一般场景模型" value="model1" />
          <el-option label="医学报告模型" value="model2" />
        </el-select>
      </el-form-item>
    </el-form>
  </div>
  <el-button type="info" plain style="width: 90%" @click="clickGenerate"
    >生成描述</el-button
  >
  <div class="ge_des">
    <el-form :model="g_description">
      <el-form-item style="font-size: 14px">
        <el-input
          placeholder="描述/报告"
          style="height: 400%"
          v-model="g_description"
        />
      </el-form-item>
    </el-form>
  </div>
  <div class="button_save">
    <el-button type="info" plain style="float: left" @click="clickSave"
      >保存描述</el-button
    >
  </div>
</template>

<script>
// import { UploadFilled } from "@element-plus/icons-vue";
import deImg from "@/assets/test.png";
export default {
  name: "EleRegister",
  data() {
    return {
      defaultImg: deImg,
      D_model: "",
      g_description: "",
    };
  },
  created() {
    this.getImage();
  },
  methods: {
    getImage() {},
    clickUserinfo() {
      const that = this;
      that.$router.push({ path: "/userInfo" });
    },
    clkicDescription() {
      const that = this;
      that.$router.push({ path: "/descriptionMan" });
    },
  },
};
</script>
<style>
.button_1 {
  font-size: 14px;
  float: left;
  position: left;
  height: 10px;
  padding-left: 25px;
  padding-bottom: 20px;
}
.button_2 {
  font-size: 14px;
  float: right;
  position: right;
  height: 10px;
  padding-right: 25px;
  padding-bottom: 20px;
}
.up_load {
  padding: 50px 10px 10px 10px;
}
.ge_des {
  padding: 20px 10px 90px 10px;
}
.button_save {
  padding: 10px 10px 10px 10px;
}
</style>
