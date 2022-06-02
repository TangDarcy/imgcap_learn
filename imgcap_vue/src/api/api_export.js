import axios from "./axios";
export default {
  //   // 不带参数的get
  //   student: () => {
  //     return axios({
  //       method: "get",
  //       url: '/student'
  //     })
  //   },
  //   // 带参数的get
  //   find_by_id: () => {
  //     return axios({
  //       method: "get",
  //       url: '/student/find_student_by_id?id=1',
  //     })
  //   },
  // 带参数的post
  find_student_by_name: () => {
    return axios({
      method: "post",
      url: "/login",
      data: {
        username: "Tang",
        password: "tang123",
      },
    });
  },
};
