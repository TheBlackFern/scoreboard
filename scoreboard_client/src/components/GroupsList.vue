/* eslint-disable */
<template>
    <div class="groups_container">
        <form @submit.prevent="changeUser">
            <input v-model="newUser" placeholder="User...">
            <button type="submit">Change</button>
        </form>
        <p v-if="currentUser === 'admin'">nice admin bro</p>

        <button @click="toggleView">Alter View</button>
        <div v-if="showOwn">
            <h1>Your Progress</h1>
            <div v-if="currentUser in userdata">
                <ul>
                    <li v-for="(group, groupName) in userdata[currentUser]" :key="groupName">
                        <p>{{ groupName }}</p>
                        <ul>
                            <li v-for="(done, task) in group" :key="task">
                                <p>{{ task }}: {{ done ? "done" : "not done" }}</p>
                            </li>
                        </ul>
                    </li>
                </ul>
            </div>
            <div v-else>
                <p>You're not a real user.</p>
            </div>
        </div>
        <div v-else class="scoreboard">
            <h1>Scoreboard</h1>
            <ul>
                <li v-for="group in groups" :key="group.id">
                    <p>{{ group.name }}</p>
                    <ul v-for="user in scoreboard[group.id]" :key="user.id">
                        <p>
                            {{ user.username === currentUser ? "You" : user.username }} : {{ user.percentage }}%
                        </p>
                    </ul>
                </li>
            </ul>
        </div>
    </div>
</template>

<script>
import axios from 'axios';
export default {
    data() {
        return {
            groups: [''],
            scoreboard: [''],
            userdata: [''],
            newUser: "",
            currentUser: "Alice",
            showOwn: true,
        }
    },
    methods: {
        changeUser() {
            this.currentUser = this.newUser;
        },

        toggleView() {
            this.showOwn = this.showOwn ? false : true;
        },

        async getData() {
            axios.get('https://scoreboard-backend-production.up.railway.app/api/groups/')
                .then((response) => {
                    this.groups = response.data;
                })
                .catch(function (error) {
                    console.log(error);
                })

            axios.get('https://scoreboard-backend-production.up.railway.app/api/usercompletion/')
                .then((response) => {
                    this.userdata = response.data;
                    console.log(this.userdata)
                })
                .catch(function (error) {
                    console.log(error);
                })

            axios.get('https://scoreboard-backend-production.up.railway.app/api/groupcompletion/')
                .then((response) => {
                    this.scoreboard = response.data;
                    for (let key in this.scoreboard) {
                        this.scoreboard[key].sort((a, b) => b.percentage - a.percentage);
                    }
                })
                .catch(function (error) {
                    console.log(error);
                })
        },
    },
    created() {
        this.getData();
    }
}
</script>