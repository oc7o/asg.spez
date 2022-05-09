<template>
    <div class="sidebar-page">
        <section class="sidebar-layout">
             <b-sidebar
                position="static"
                :mobile="mobile"
                :expand-on-hover="expandOnHover"
                :reduce="reduce"
                :delay="expandWithDelay ? 500 : null"
                type="is-light"
                open
            >
                <div class="p-1">
                    <div class="block">
                    <img
                        src="https://raw.githubusercontent.com/buefy/buefy/dev/static/img/buefy-logo.png"
                        alt="Lightweight UI components for Vue.js based on Bulma"
                    />
                    </div>
                    <b-menu class="is-custom-mobile">
                        <b-menu-list label="Menu">
                            <b-menu-item icon="information-outline" label="Info"></b-menu-item>
                            <b-menu-item active expanded icon="settings" label="Administrator">
                                <b-menu-item icon="account" label="Users"></b-menu-item>
                                <b-menu-item icon="cellphone-link" label="Devices"></b-menu-item>
                                <b-menu-item icon="cash-multiple" label="Payments" disabled></b-menu-item>
                            </b-menu-item>
                            <b-menu-item icon="account" label="My Account">
                                <b-menu-item icon="account-box" label="Account data"></b-menu-item>
                                <b-menu-item icon="home-account" label="Addresses"></b-menu-item>
                            </b-menu-item>
                        </b-menu-list>
                        <b-menu-list>
                            <b-menu-item label="Expo" icon="link"></b-menu-item>
                        </b-menu-list>
                        <b-menu-list label="Actions">
                            <b-menu-item icon="logout" label="Logout"></b-menu-item>
                        </b-menu-list>
                    </b-menu>
                </div>
            </b-sidebar>

            <div class="p-1">
                <b-field>
                    <b-switch v-model="reduce">Reduced</b-switch>
                </b-field>
                <b-field>
                    <b-switch v-model="expandOnHover">Expand on hover</b-switch>
                </b-field>
                <b-field>
                    <b-switch v-model="expandWithDelay">Hover with delay</b-switch>
                </b-field>
                <b-field label="Mobile Layout">
                    <b-select v-model="mobile">
                        <option :value="null"></option>
                        <option value="reduce">Reduced</option>
                        <option value="hide">Hidden</option>
                        <option value="fullwidth">Fullwidth</option>
                    </b-select>
                </b-field>
            </div>
        </section>
    </div>
</template>