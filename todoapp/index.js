const request_url = "http://localhost:5000/api/todoitems";
const bus = new Vue();

Vue.component("show-todo-items", {
  data: function () { return { items: null }; },
  methods: {
    showtodo: function () {
      fetch(request_url)
        .then(response => response.json())
        .then(jsondata => this.items = jsondata.objects);
    }
  },
  mounted: function () {
    this.showtodo();
    bus.$on("on-item-registered", this.showtodo);
  },
  template: '<ul><li v-for="item in items">{{ item.title }}</li></ul>'
});

Vue.component("register-todo-item", {
  data: function () { return { todotitle: "" }; },
  template:
    `<div>
      <input v-model="todotitle">
      <button v-on:click="register_todoitem(todotitle)">Register todo item</button>
    </div>`,
  methods: {
    register_todoitem: function(todotitle) {
      console.log(todotitle);
      fetch(request_url, {
        method: "POST",
        mode: "cors",
        body: JSON.stringify({ title: todotitle }),
        headers: {
          "content-type": "application/json"
        }
      })
        .then(response => response.json())
        .then(jsondata => {
          console.log(jsondata);
          bus.$emit("on-item-registered", jsondata);
        })
        .catch(err => console.log(`err: ${err}`));
    }
  }
});

var app = new Vue({
  el: '#app'
});

