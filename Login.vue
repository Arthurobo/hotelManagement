<template>
      <v-container class="fill-height" fluid >
        <v-row align="center" justify="center" >
          <v-col cols="12" sm="8" md="4">
            <v-card class="elevation-10">
              <v-toolbar color="primary" dark flat>
                <v-toolbar-title class="center-login">Login</v-toolbar-title>
              </v-toolbar>
              <v-card-text>
                <h1 v-if="incorrectAuth">Incorrect username or password entered - Try again</h1>
                <v-form v-on:submit.prevent="login">
                  <v-text-field v-model="username" label="Username" prepend-icon="mdi-account" type="text"></v-text-field>
                  <v-text-field v-model="password" id="password" label="Password"  prepend-icon="mdi-lock" type="password"></v-text-field>
                <v-btn color="primary" type="submit">Login</v-btn>
                </v-form>
              </v-card-text>
              <v-card-actions>
                <v-spacer></v-spacer>
              </v-card-actions>
            </v-card>
          </v-col>
        </v-row>
      </v-container>
</template>

<script>
  export default {
    name: 'login',
    data () {
      return {
        username: '',
        password: '',
        incorrectAuth: false
      }
    },
    methods: {
      login () { 
        this.$store.dispatch('userLogin', {
          username: this.username,
          password: this.password
        })
        .then(() => {
          this.$router.push({ name: 'home' })
        })
        .catch(err => {
          console.log(err)
          this.incorrectAuth = true
        })
        }
      }
  }

</script>
<style>
    .nav-wrapper {
        background: #333;
    }

    .nav-list-item {
        background: #333;
    }

    .center-login {
        text-align: center;
    }
</style>