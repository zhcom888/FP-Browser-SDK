from .permission_type import PermissionType

PermissionType88 = {
    # "DEFAULT" is only used as an argument to the Content Settings Window
    # opener; there it means "whatever was last shown".
    PermissionType.DEFAULT: -1,
    PermissionType.COOKIES: 0,
    PermissionType.IMAGES: 1,
    PermissionType.JAVASCRIPT: 2,
    PermissionType.PLUGINS: 3,

    # This setting governs both popups and unwanted redirects like tab-unders and
    # framebusting.
    # TODO(csharrison): Consider renaming it to POPUPS_AND_REDIRECTS, but it
    # might not be worth the trouble.
    PermissionType.POPUPS: 4,

    PermissionType.GEOLOCATION: 5,
    PermissionType.NOTIFICATIONS: 6,
    PermissionType.AUTO_SELECT_CERTIFICATE: 7,
    PermissionType.MIXEDSCRIPT: 8,
    PermissionType.MEDIASTREAM_MIC: 9,
    PermissionType.MEDIASTREAM_CAMERA: 10,
    PermissionType.PROTOCOL_HANDLERS: 11,
    PermissionType.PPAPI_BROKER: 12,
    PermissionType.AUTOMATIC_DOWNLOADS: 13,
    PermissionType.MIDI_SYSEX: 14,
    PermissionType.SSL_CERT_DECISIONS: 15,
    PermissionType.PROTECTED_MEDIA_IDENTIFIER: 16,
    PermissionType.APP_BANNER: 17,
    PermissionType.SITE_ENGAGEMENT: 18,
    PermissionType.DURABLE_STORAGE: 19,
    PermissionType.USB_CHOOSER_DATA: 20,
    PermissionType.BLUETOOTH_GUARD: 21,
    PermissionType.BACKGROUND_SYNC: 22,
    PermissionType.AUTOPLAY: 23,
    PermissionType.IMPORTANT_SITE_INFO: 24,
    PermissionType.PERMISSION_AUTOBLOCKER_DATA: 25,
    PermissionType.ADS: 26,

    # Website setting which stores metadata for the subresource filter to aid in
    # decisions for whether or not to show the UI.
    PermissionType.ADS_DATA: 27,

    # This is special-cased in the permissions layer to always allow, and as
    # such doesn't have associated prefs data.
    PermissionType.MIDI: 28,

    # This content setting type is for caching password protection service's
    # verdicts of each origin.
    PermissionType.PASSWORD_PROTECTION: 29,

    # Website setting which stores engagement data for media related to a
    # specific origin.
    PermissionType.MEDIA_ENGAGEMENT: 30,

    # Content setting which stores whether or not the site can play audible
    # sound. This will not block playback but instead the user will not hear it.
    PermissionType.SOUND: 31,

    # Website setting which stores the list of client hints (and the preference
    # expiration time for each of the client hints) that the origin requested
    # the browser to remember. Spec:
    # http://httpwg.org/http-extensions/client-hints.html#accept-ch-lifetime.
    # The setting is stored as a dictionary that includes the mapping from
    # different client hints to their respective expiration times (seconds since
    # epoch). The browser is expected to send all the unexpired client hints in
    # the HTTP request headers for every resource requested from that origin.
    PermissionType.CLIENT_HINTS: 32,

    # Generic Sensor API covering ambient-light-sensor, accelerometer, gyroscope
    # and magnetometer are all mapped to a single content_settings_type.
    # Setting for the Generic Sensor API covering ambient-light-sensor,
    # accelerometer, gyroscope and magnetometer. These are all mapped to a single
    # ContentSettingsType.
    PermissionType.SENSORS: 33,

    # Content setting which stores whether or not the user has granted the site
    # permission to respond to accessibility events, which can be used to
    # provide a custom accessibility experience. Requires explicit user consent
    # because some users may not want sites to know they're using assistive
    # technology.
    PermissionType.ACCESSIBILITY_EVENTS: 34,

    # Used to store whether to allow a website to install a payment handler.
    PermissionType.PAYMENT_HANDLER: 35,

    # Content setting which stores whether to allow sites to ask for permission
    # to access USB devices. If this is allowed specific device permissions are
    # stored under USB_CHOOSER_DATA.
    PermissionType.USB_GUARD: 36,

    # Nothing is stored in this setting at present. Please refer to
    # BackgroundFetchPermissionContext for details on how this permission
    # is ascertained.
    PermissionType.BACKGROUND_FETCH: 37,

    # Website setting which stores the amount of times the user has dismissed
    # intent picker UI without explicitly choosing an option.
    PermissionType.INTENT_PICKER_DISPLAY: 38,

    # Used to store whether to allow a website to detect user active/idle state.
    PermissionType.IDLE_DETECTION: 39,

    # Content settings for access to serial ports. The "guard" content setting
    # stores whether to allow sites to ask for permission to access a port. The
    # permissions granted to access particular ports are stored in the "chooser
    # data" website setting.
    PermissionType.SERIAL_GUARD: 40,
    PermissionType.SERIAL_CHOOSER_DATA: 41,

    # Nothing is stored in this setting at present. Please refer to
    # PeriodicBackgroundSyncPermissionContext for details on how this permission
    # is ascertained.
    PermissionType.PERIODIC_BACKGROUND_SYNC: 42,

    # Content setting which stores whether to allow sites to ask for permission
    # to do Bluetooth scanning.
    PermissionType.BLUETOOTH_SCANNING: 43,

    # Content settings for access to HID devices. The "guard" content setting
    # stores whether to allow sites to ask for permission to access a device. The
    # permissions granted to access particular devices are stored in the "chooser
    # data" website setting.
    PermissionType.HID_GUARD: 44,
    PermissionType.HID_CHOOSER_DATA: 45,

    # Wake Lock API, which has two lock types: screen and system locks.
    # Currently, screen locks do not need any additional permission, and system
    # locks are always denied while the right UI is worked out.
    PermissionType.WAKE_LOCK_SCREEN: 46,
    PermissionType.WAKE_LOCK_SYSTEM: 47,

    # Legacy SameSite cookie behavior. This disables SameSiteByDefaultCookies,
    # CookiesWithoutSameSiteMustBeSecure, and SchemefulSameSite, forcing the
    # legacy behavior wherein cookies that don't specify SameSite are treated as
    # SameSite=None, SameSite=None cookies are not required to be Secure, and
    # schemeful same-site is not active.
    #
    # This will also be used to revert to legacy behavior when future changes
    # in cookie handling are introduced.
    PermissionType.LEGACY_COOKIE_ACCESS: 48,

    # Content settings which stores whether to allow sites to ask for permission
    # to save changes to an original file selected by the user through the
    # File System API.
    PermissionType.FILE_SYSTEM_WRITE_GUARD: 49,

    # Content settings for installed web apps that browsing history may be
    # inferred from e.g. last update check timestamp.
    PermissionType.INSTALLED_WEB_APP_METADATA: 50,

    # Used to store whether to allow a website to exchange data with NFC devices.
    PermissionType.NFC: 51,

    # Website setting to store permissions granted to access particular Bluetooth
    # devices.
    PermissionType.BLUETOOTH_CHOOSER_DATA: 52,

    # Full access to the system clipboard (sanitized read without user gesture,
    # and unsanitized read and write with user gesture).
    # TODO(https://crbug.com/1027225): Move CLIPBOARD_READ_WRITE uses to be
    # ordered in the same order as listed in the enum.
    PermissionType.CLIPBOARD_READ_WRITE: 53,

    # This is special-cased in the permissions layer to always allow, and as
    # such doesn't have associated prefs data.
    # TODO(https://crbug.com/1027225): Move CLIPBOARD_SANITIZED_WRITE uses to be
    # ordered in the same order as listed in the enum.
    PermissionType.CLIPBOARD_SANITIZED_WRITE: 54,

    # This content setting type is for caching safe browsing real time url
    # check's verdicts of each origin.
    PermissionType.SAFE_BROWSING_URL_CHECK_DATA: 55,

    # Used to store whether a site is allowed to request AR or VR sessions with
    # the WebXr Device API.
    PermissionType.VR: 56,
    PermissionType.AR: 57,

    # Content setting which stores whether to allow site to open and read files
    # and directories selected through the File System API.
    PermissionType.FILE_SYSTEM_READ_GUARD: 58,

    # Access to first party storage in a third-party context. Exceptions are
    # scoped to the combination of requesting/top-level origin, and are managed
    # through the Storage Access API. For the time being, this content setting
    # exists in parallel to third-party cookie rules stored in COOKIES.
    # TODO(https://crbug.com/989663): Reconcile the two.
    PermissionType.STORAGE_ACCESS: 59,

    # Content setting which stores whether to allow a site to control camera
    # movements. It does not give access to camera.
    PermissionType.CAMERA_PAN_TILT_ZOOM: 60,

    # Content setting for Screen Enumeration and Window Placement functionality.
    # Permits access to information about the screens, like size and position.
    # Permits creating and placing windows across the set of connected screens.
    PermissionType.WINDOW_PLACEMENT: 61,

    # Stores whether to allow insecure websites to make private network requests.
    # See also: https://wicg.github.io/cors-rfc1918
    # Set through enterprise policies only.
    PermissionType.INSECURE_PRIVATE_NETWORK: 62,

    # Content setting which stores whether or not a site can access low-level
    # locally installed font data using the Font Access API.
    PermissionType.FONT_ACCESS: 63,

    # Stores per-origin state for permission auto-revocation (for all permission
    # types).
    PermissionType.PERMISSION_AUTOREVOCATION_DATA: 64,

    # Stores per-origin state of the most recently selected directory for the use
    # by the File System Access API.
    PermissionType.FILE_SYSTEM_LAST_PICKED_DIRECTORY: 65,

    PermissionType.NUM_TYPES: 66,
}
