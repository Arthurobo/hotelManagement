<template>

<v-container fluid>
            <v-row>
          <v-col align="center" cols="3" v-for="business in Businesses" :key="business.id">
        <v-card class="" width="250">
          <!-- <v-img class="white--text align-end" height="200px" :src="job.image ">
          </v-img> -->
        <v-avatar align="left" style="margin-top: 5px; border-radius: 40px" class="profile-icon">
          <img :src="business.image" alt="John">
        </v-avatar>
            
            
          <router-link v-bind:to="'/businesses/' + business.id">
    <v-card-text>
      <div>
        <h3>{{ business.page_name }}</h3>
      </div>
      <div>
        <h4 class="business-category">{{ business.category_of_business }}</h4>
        <h4 class="city_location_of_page"> {{ business.city_location_of_page }}</h4>
      </div>
      <div><h4>{{ business.type_of_business }}</h4></div>
      <div>{{ business.office_address }}</div>
    </v-card-text>
          </router-link>
          <v-card-actions align="center">
          </v-card-actions>
        </v-card>  
          </v-col>
        </v-row>
  </v-container>

    <!-- user
page_name
page_description
country_location_of_page
state_location_of_page
city_location_of_page
office_address
ip_address
zip_code
type_of_business
category_of_business -->
</template>

<script>
import axios from 'axios'

export default {
    data () {
        return {
            Businesses: null,
        }
    },

    mounted () {
        axios
        .get('http://127.0.0.1:8000/api/business-pages/nearby-businesses/',)
        .then(response => (
            this.Businesses = response.data
        ))
        .catch(e => {
            this.errors.push(e)
        })
      
    },
};
</script>


<style scoped>
.business-category {
  background-color: #f2f2f2;
  border-radius: 50px;
  padding: 3px 0px;
}

.city_location_of_page {
  color: blue
}
</style>






  