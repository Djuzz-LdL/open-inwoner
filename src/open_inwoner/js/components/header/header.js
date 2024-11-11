import BEM from 'bem.js'
import { Component } from '../abstract/component'

/** @type {string} Header block name. */
export const BLOCK_HEADER = 'header__button'

/** @type {string} Modifier describing open state. */
export const MODIFIER_DISMISSED = 'dismissed'

/** @type {NodeList<HTMLElement>} The primary navigation block name. */
export const HEADERS = BEM.getBEMNodes(BLOCK_HEADER)

/** Handler to bypass Safari bug */
export const themesToggle = document.querySelectorAll('.dropdown-nav__toggle')

/** Controls aria-expanded state for accessibility */
export const interactiveButton = document.querySelectorAll('.header__button')

/**
 * Controls the main header and interaction with the mobile menu and dismissing it using the escape key.
 */
class Header extends Component {
  constructor(node, initialState = { dismissed: false }) {
    super(node, initialState)
  }

  /**
   * Binds events to callbacks.
   * Callbacks should trigger `setState` which in turn triggers `render`.
   * Focus is split to be handled in Safari
   */
  bindEvents() {
    this.node.addEventListener('click', this.toggleMobileNavOpen.bind(this))
    this.node.addEventListener('focusout', this.onFocusMobileOut.bind(this))
    window.addEventListener('keyup', this.onEscape.bind(this))

    const closeMobileNav = document.getElementById('closeMobileNav') // Use ID to reference the close button
    if (closeMobileNav) {
      closeMobileNav.addEventListener('click', this.closeMenu.bind(this))
    }
  }

  /**
   * Gets called when `node` receives focus -in or -out events.
   * Clears the dismissed state, (prevents overriding focus/hover).
   * Focusin and Focusout are used instead of Focus for Safari
   */
  onFocusMobileOut() {
    // Safari specific
    this.setState({ dismissed: true })
  }

  /**
   * Gets called when `node` is clicked.
   * Clears the dismissed state, (prevents overriding focus/toggle).
   */
  toggleMobileNavOpen() {
    document.body.classList.toggle('body--open')
    // Safari specific - close all when main menu closes
    themesToggle.forEach((elem) => {
      elem.classList.remove('nav__list--open')
    })
    interactiveButton.forEach((elem) => {
      elem.setAttribute(
        'aria-expanded',
        elem.getAttribute('aria-expanded') === 'true' ? 'false' : 'true'
      )
    })
    window.scrollTo(0, 0)

    // Focus on the first navigation item in opened mobile menu
    const firstNavItem = document.querySelector(
      '.primary-navigation__list-item .link'
    )
    if (firstNavItem) {
      firstNavItem.focus()
    }
  }

  /**
   * Only if body--open exists, handle close-button.
   */
  closeMenu() {
    if (document.body.classList.contains('body--open')) {
      document.body.classList.remove('body--open')
    }
  }

  /**
   * Gets called when a key is released.
   * If key is escape key, explicitly close the mobile menu.
   * @param {KeyboardEvent} event
   */
  onEscape(event) {
    if (event.key === 'Escape') {
      this.setState({ dismissed: true })
      this.node.blur()
      document.body.classList.remove('body--open')
    }
  }

  /**
   * Persists state to DOM.
   * Rendering should be one-way traffic and not inspect any current values in DOM.
   //* @param {Object} state State to render.
   */
  render(state) {
    document.body.classList.add('body')
    BEM.toggleModifier(this.node, MODIFIER_DISMISSED, state.dismissed)

    if (state.dismissed) {
      this.node.blur()

      return this.node.querySelector('.header__button')
    }
  }
}

// Start!
;[...HEADERS].forEach((node) => new Header(node, { dismissed: false }))
