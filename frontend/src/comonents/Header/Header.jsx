import React from 'react';
import { NavLink } from 'react-router-dom';
import styles from './Header.module.css'

const Header = () => {
	return (
		<header className={styles.header}>
			<div className={styles.container}>
				<nav className={styles.topNav}>
					<ul className={styles.navLeft}>
						<a href="http://" target="_blank" ></a>
						<a href="http://" target="_blank" ></a>
						<a href="http://" target="_blank" ></a>
					</ul>
				</nav>
			</div>
		</header>
	);
};

export default Header;