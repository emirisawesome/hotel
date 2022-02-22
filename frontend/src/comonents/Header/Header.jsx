import React from 'react';
import { NavLink } from 'react-router-dom';
import styles from './Header.module.css'
import { FaTwitter } from "react-icons/fa";
import { FaFacebookF } from "react-icons/fa";
import { FaYoutube } from "react-icons/fa";

const Header = () => {
	return (
		<header className={styles.header}>
			<div className={styles.container}>
				<nav className={styles.topNav}>
					<ul className={styles.navLeft}>
						<a href="http://" target="_blank" >
							<FaFacebookF className={styles.topnav} />
						</a>
						<a href="http://" target="_blank" >
							<FaTwitter className={styles.topnav} />
						</a>
						<a href="http://" target="_blank" >
							<FaYoutube className={styles.topnav} />
						</a>
					</ul>
					<ul className={styles.navLeft}>
						<a href="http://" target="_blank" >
							<FaFacebookF className={styles.topnav} />
						</a>
						<a href="http://" target="_blank" >
							<FaTwitter className={styles.topnav} />
						</a>
						<a href="http://" target="_blank" >
							<FaYoutube className={styles.topnav} />
						</a>
					</ul>
				</nav>
			</div>
		</header>
	);
};

export default Header;