from enum import Enum, unique


@unique
class PermissionType(Enum):
    DEFAULT = 'DEFAULT',
    COOKIES = 'COOKIES',
    IMAGES = 'IMAGES',
    JAVASCRIPT = 'JAVASCRIPT',
    PLUGINS = 'PLUGINS',
    DEPRECATED_PLUGINS = 'DEPRECATED_PLUGINS',

    # This setting governs both popups and unwanted redirects like tab-unders and
    # framebusting.
    # TODO(csharrison): Consider renaming it to POPUPS_AND_REDIRECTS, but it
    # might not be worth the trouble.
    POPUPS = 'POPUPS',

    GEOLOCATION = 'GEOLOCATION',  # 4
    NOTIFICATIONS = 'NOTIFICATIONS',  # 5
    AUTO_SELECT_CERTIFICATE = 'AUTO_SELECT_CERTIFICATE',  # 6
    MIXEDSCRIPT = 'MIXEDSCRIPT',  # 7
    MEDIASTREAM_MIC = 'MEDIASTREAM_MIC',  # 8
    MEDIASTREAM_CAMERA = 'MEDIASTREAM_CAMERA',  # 9
    PROTOCOL_HANDLERS = 'PROTOCOL_HANDLERS',  # 10
    PPAPI_BROKER = 'PPAPI_BROKER',  # 11
    AUTOMATIC_DOWNLOADS = 'AUTOMATIC_DOWNLOADS',  # 12
    MIDI_SYSEX = 'MIDI_SYSEX',  # 13
    SSL_CERT_DECISIONS = 'SSL_CERT_DECISIONS',  # 14
    PROTECTED_MEDIA_IDENTIFIER = 'PROTECTED_MEDIA_IDENTIFIER',  # 15
    APP_BANNER = 'APP_BANNER',  # 16
    SITE_ENGAGEMENT = 'SITE_ENGAGEMENT',  # 17
    DURABLE_STORAGE = 'DURABLE_STORAGE',  # 18
    USB_CHOOSER_DATA = 'USB_CHOOSER_DATA',  # 19
    BLUETOOTH_GUARD = 'BLUETOOTH_GUARD',  # 20
    BACKGROUND_SYNC = 'BACKGROUND_SYNC',  # 21
    AUTOPLAY = 'AUTOPLAY',  # 22
    IMPORTANT_SITE_INFO = 'IMPORTANT_SITE_INFO',  # 23
    PERMISSION_AUTOBLOCKER_DATA = 'PERMISSION_AUTOBLOCKER_DATA',  # 24
    ADS = 'ADS',  # 25

    # Website setting which stores metadata for the subresource filter to aid in
    # decisions for whether or not to show the UI.
    ADS_DATA = 'ADS_DATA',  # 26

    # This is special-cased in the permissions layer to always allow, and as
    # such doesn't have associated prefs data.
    MIDI = 'MIDI',  # 27

    # This content setting type is for caching password protection service's
    # verdicts of each origin.
    PASSWORD_PROTECTION = 'PASSWORD_PROTECTION',  # 28

    # Website setting which stores engagement data for media related to a
    # specific origin.
    MEDIA_ENGAGEMENT = 'MEDIA_ENGAGEMENT',  # 29

    # Content setting which stores whether or not the site can play audible
    # sound. This will not block playback but instead the user will not hear it.
    SOUND = 'SOUND',  # 30

    # Website setting which stores the list of client hints that the origin
    # requested the browser to remember. The browser is expected to send all
    # client hints in the HTTP request headers for every resource requested
    # from that origin.
    CLIENT_HINTS = 'CLIENT_HINTS',  # 31

    # Generic Sensor API covering ambient-light-sensor, accelerometer, gyroscope
    # and magnetometer are all mapped to a single content_settings_type.
    # Setting for the Generic Sensor API covering ambient-light-sensor,
    # accelerometer, gyroscope and magnetometer. These are all mapped to a single
    # ContentSettingsType.
    SENSORS = 'SENSORS',  # 32

    # Content setting which stores whether or not the user has granted the site
    # permission to respond to accessibility events, which can be used to
    # provide a custom accessibility experience. Requires explicit user consent
    # because some users may not want sites to know they're using assistive
    # technology.
    ACCESSIBILITY_EVENTS = 'ACCESSIBILITY_EVENTS',  # 33

    # Used to store whether to allow a website to install a payment handler.
    PAYMENT_HANDLER = 'PAYMENT_HANDLER',  # 34

    # Content setting which stores whether to allow sites to ask for permission
    # to access USB devices. If this is allowed specific device permissions are
    # stored under USB_CHOOSER_DATA.
    USB_GUARD = 'USB_GUARD',  # 35

    # Nothing is stored in this setting at present. Please refer to
    # BackgroundFetchPermissionContext for details on how this permission
    # is ascertained.
    BACKGROUND_FETCH = 'BACKGROUND_FETCH',  # 36

    # Website setting which stores the amount of times the user has dismissed
    # intent picker UI without explicitly choosing an option.
    INTENT_PICKER_DISPLAY = 'INTENT_PICKER_DISPLAY',  # 37

    # Used to store whether to allow a website to detect user active/idle state.
    IDLE_DETECTION = 'IDLE_DETECTION',  # 38

    # Setting for enabling auto-select of all screens for getDisplayMediaSet.
    GET_DISPLAY_MEDIA_SET_SELECT_ALL_SCREENS = 'GET_DISPLAY_MEDIA_SET_SELECT_ALL_SCREENS',  # 39

    # Content settings for access to serial ports. The "guard" content setting
    # stores whether to allow sites to ask for permission to access a port. The
    # permissions granted to access particular ports are stored in the "chooser
    # data" website setting.
    SERIAL_GUARD = 'SERIAL_GUARD',  # 40
    SERIAL_CHOOSER_DATA = 'SERIAL_CHOOSER_DATA',  # 41

    # Nothing is stored in this setting at present. Please refer to
    # PeriodicBackgroundSyncPermissionContext for details on how this permission
    # is ascertained.
    # This content setting is not registered because it does not require access
    # to any existing providers.
    PERIODIC_BACKGROUND_SYNC = 'PERIODIC_BACKGROUND_SYNC',  # 42

    # Content setting which stores whether to allow sites to ask for permission
    # to do Bluetooth scanning.
    BLUETOOTH_SCANNING = 'BLUETOOTH_SCANNING',  # 43

    # Content settings for access to HID devices. The "guard" content setting
    # stores whether to allow sites to ask for permission to access a device. The
    # permissions granted to access particular devices are stored in the "chooser
    # data" website setting.
    HID_GUARD = 'HID_GUARD',  # 44
    HID_CHOOSER_DATA = 'HID_CHOOSER_DATA',  # 45

    # Wake Lock API, which has two lock types: screen and system locks.
    # Currently, screen locks do not need any additional permission, and system
    # locks are always denied while the right UI is worked out.
    WAKE_LOCK_SCREEN = 'WAKE_LOCK_SCREEN',  # 46
    WAKE_LOCK_SYSTEM = 'WAKE_LOCK_SYSTEM',  # 47

    # Legacy SameSite cookie behavior. This disables SameSite=Lax-by-default,
    # SameSite=None requires Secure, and Schemeful Same-Site, forcing the
    # legacy behavior wherein 1) cookies that don't specify SameSite are treated
    # as SameSite=None, 2) SameSite=None cookies are not required to be Secure,
    # and 3) schemeful same-site is not active.
    #
    # This will also be used to revert to legacy behavior when future changes
    # in cookie handling are introduced.
    LEGACY_COOKIE_ACCESS = 'LEGACY_COOKIE_ACCESS',  # 48

    # Content settings which stores whether to allow sites to ask for permission
    # to save changes to an original file selected by the user through the
    # File System Access API.
    FILE_SYSTEM_WRITE_GUARD = 'FILE_SYSTEM_WRITE_GUARD',  # 49

    # Content settings for installed web apps that browsing history may be
    # inferred from e.g. last update check timestamp.
    INSTALLED_WEB_APP_METADATA = 'INSTALLED_WEB_APP_METADATA',  # 50

    # Used to store whether to allow a website to exchange data with NFC devices.
    NFC = 'NFC',  # 51

    # Website setting to store permissions granted to access particular Bluetooth
    # devices.
    BLUETOOTH_CHOOSER_DATA = 'BLUETOOTH_CHOOSER_DATA',  # 52

    # Full access to the system clipboard (sanitized read without user gesture,
    # and unsanitized read and write with user gesture).
    # TODO(https:#crbug.com/1027225): Move CLIPBOARD_READ_WRITE uses to be
    # ordered in the same order as listed in the enum.
    CLIPBOARD_READ_WRITE = 'CLIPBOARD_READ_WRITE',  # 53

    # This is special-cased in the permissions layer to always allow, and as
    # such doesn't have associated prefs data.
    # TODO(https:#crbug.com/1027225): Move CLIPBOARD_SANITIZED_WRITE uses to be
    # ordered in the same order as listed in the enum.
    CLIPBOARD_SANITIZED_WRITE = 'CLIPBOARD_SANITIZED_WRITE',  # 54

    # This content setting type is for caching safe browsing real time url
    # check's verdicts of each origin.
    SAFE_BROWSING_URL_CHECK_DATA = 'SAFE_BROWSING_URL_CHECK_DATA',  # 55

    # Used to store whether a site is allowed to request AR or VR sessions with
    # the WebXr Device API.
    VR = 'VR',  # 56
    AR = 'AR',  # 57

    # Content setting which stores whether to allow site to open and read files
    # and directories selected through the File System Access API.
    FILE_SYSTEM_READ_GUARD = 'FILE_SYSTEM_READ_GUARD',  # 58

    # Access to first party storage in a third-party context. Exceptions are
    # scoped to the combination of requesting/top-level origin, and are managed
    # through the Storage Access API. For the time being, this content setting
    # exists in parallel to third-party cookie rules stored in COOKIES.
    # TODO(https:#crbug.com/989663): Reconcile the two.
    STORAGE_ACCESS = 'STORAGE_ACCESS',  # 59

    # Content setting which stores whether to allow a site to control camera
    # movements. It does not give access to camera.
    CAMERA_PAN_TILT_ZOOM = 'CAMERA_PAN_TILT_ZOOM',  # 60

    # Content setting for Screen Enumeration and Window Placement functionality.
    # Permits access to information about the screens, like size and position.
    # Permits creating and placing windows across the set of connected screens.
    WINDOW_PLACEMENT = 'WINDOW_PLACEMENT',  # 61

    # Stores whether to allow insecure websites to make private network requests.
    # See also: https:#wicg.github.io/cors-rfc1918
    # Set through enterprise policies only.
    INSECURE_PRIVATE_NETWORK = 'INSECURE_PRIVATE_NETWORK',  # 62

    # Content setting which stores whether or not a site can access low-level
    # locally installed font data using the Local Fonts Access API.
    LOCAL_FONTS = 'LOCAL_FONTS',  # 63
    FONT_ACCESS = 'FONT_ACCESS',  # 63

    # Stores per-origin state for permission auto-revocation (for all permission
    # types).
    PERMISSION_AUTOREVOCATION_DATA = 'PERMISSION_AUTOREVOCATION_DATA',  # 64

    # Stores per-origin state of the most recently selected directory for the use
    # by the File System Access API.
    FILE_SYSTEM_LAST_PICKED_DIRECTORY = 'FILE_SYSTEM_LAST_PICKED_DIRECTORY',  # 65

    # Controls access to the getDisplayMedia API when {preferCurrentTab: true}
    # is specified.
    # TODO(crbug.com/1150788): Also apply this when getDisplayMedia() is called
    # without specifying {preferCurrentTab: true}.
    # No values are stored for this type, this is solely needed to be able to
    # register the PermissionContext.
    DISPLAY_CAPTURE = 'DISPLAY_CAPTURE',  # 66

    # Register file-type associations with the operating system and obtain
    # read-only access to files that the user chooses to open with this
    # installed web application from the system file manager. This setting has
    # no effect on the File System API, <input type="file">, or the ability to
    # access files through drag & drop or clipboard paste operations.
    FILE_HANDLING = 'FILE_HANDLING',

    # Website setting to store permissions metadata granted to paths on the local
    # file system via the File System Access API. |FILE_SYSTEM_WRITE_GUARD| is
    # the corresponding "guard" setting.
    FILE_SYSTEM_ACCESS_CHOOSER_DATA = 'FILE_SYSTEM_ACCESS_CHOOSER_DATA',  # 67

    # Stores a grant for the browser to intermediate or allow without
    # restriction sharing of identity information by an identity provider to
    # specified relying parties. The setting is associated with the identity
    # provider's origin.
    # This is managed by WebID.
    FEDERATED_IDENTITY_SHARING = 'FEDERATED_IDENTITY_SHARING',  # 68

    # Stores a grant that allows a relying party to send a request for identity
    # information to specified identity providers, potentially through any
    # anti-tracking measures that would otherwise prevent it. This setting is
    # associated with the relying party's origin.
    FEDERATED_IDENTITY_REQUEST = 'FEDERATED_IDENTITY_REQUEST',  # 69

    # Whether to use the v8 optimized JIT for running JavaScript on the page.
    JAVASCRIPT_JIT = 'JAVASCRIPT_JIT',  # 70

    # Content setting which stores user decisions to allow loading a site over
    # HTTP. Entries are added by hostname when a user bypasses the HTTPS-First
    # Mode interstitial warning when a site does not support HTTPS. Allowed hosts
    # are exact hostname matches -- subdomains of a host on the allowlist must be
    # separately allowlisted.
    HTTP_ALLOWED = 'HTTP_ALLOWED',  # 71

    # Stores metadata related to form fill, such as e.g. whether user data was
    # autofilled on a specific website.
    FORMFILL_METADATA = 'FORMFILL_METADATA',  # 72

    # Setting to indicate that there is an active federated sign-in session
    # between a specified relying party and a specified identity provider for
    # a specified account. When this is present it allows access to session
    # management capabilities between the sites. This setting is associated
    # with the relying party's origin.
    FEDERATED_IDENTITY_ACTIVE_SESSION = 'FEDERATED_IDENTITY_ACTIVE_SESSION',  # 73

    # Setting to indicate whether Chrome should automatically apply darkening to
    # web content.
    AUTO_DARK_WEB_CONTENT = 'AUTO_DARK_WEB_CONTENT',  # 74

    # Setting to indicate whether Chrome should request the desktop view of a
    # site instead of the mobile one.
    REQUEST_DESKTOP_SITE = 'REQUEST_DESKTOP_SITE',  # 75

    # Setting to indicate whether browser should allow signing into a website via
    # the browser FedCM API.
    FEDERATED_IDENTITY_API = 'FEDERATED_IDENTITY_API',  # 76

    NUM_TYPES = 'NUM_TYPES',  # 77
