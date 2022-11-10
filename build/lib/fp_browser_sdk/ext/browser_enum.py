from enum import Enum, unique


@unique
class BaseEnum(str, Enum):
    NULL = "null"


@unique
class MediaKind(int, Enum):
    AUDIO_INPUT = 0
    AUDIO_OUTPUT = 1
    VIDEO_INPUT = 2


@unique
class PrefersColor(str, Enum):
    LIGHT = "light"
    DARK = "dark"


@unique
class CompatMode(str, Enum):
    CSS1COMPAT = "CSS1Compat"
    BACKCOMPAT = "BackCompat"


@unique
class VideoSupportType(str, Enum):
    EMPTY = ""
    MAYBE = "maybe"
    PROBABLY = "probably"


@unique
class MatchType(int, Enum):
    FULL = 1
    RE = 2
    PATH = 3


@unique
class ScreenOrientationType(Enum):
    LANDSCAPE_SECONDARY = ('landscape-secondary', 270)
    LANDSCAPE_PRIMARY = ('landscape-primary', 90)
    PORTRAIT_PRIMARY = ('portrait-primary', 0)


@unique
class ScreenColorDepth(int, Enum):
    ColorDepth_24 = 24
    ColorDepth_30 = 30


@unique
class Floatinfinity(str, Enum):
    INFINITY = 'infinity'


@unique
class TLSVersion(str, Enum):
    TLS_1 = 'tls1'
    TLS_1_1 = 'tls1.1'
    TLS_1_2 = 'tls1.2'
    TLS_1_3 = 'tls1.3'


@unique
class SpeechSynthesisVoiceAppendMode(str, Enum):
    INSERT = 'insert'
    PUSH = 'push'


@unique
class PerformanceNavigationType(int, Enum):
    NAVIGATE = 0
    RELOAD = 1
    BACK_FORWARD = 2
    RESERVED = 255


@unique
class DoNotTrackType(str, Enum):
    ON = '1'
    OFF = '0'
    UNSPECIFIED = 'unspecified'


@unique
class MaxTouchPoint(int, Enum):
    MOBILE = 5
    PC = 1


@unique
class WebClientHintsType(int, Enum):
    # Enumerator values are logged in UMA histograms and must not be changed.
    # Hints may be removed from this list, so if you need the total count call
    # network::GetClientHintToNameMap().size() and don't use kMaxValue.

    # Warning: The list of client hints to be persisted for a given origin are
    # sent by the renderer process to the browser process. This makes it possible
    # for a malicious renderer to change the list of client hints to be sent to
    # arbitrary origins. As such, this list should not include any client hint
    # that provides user identification information, or anything that can be
    # considered as privacy sensitive information.
    # Additionally, all client hints headers are considered as CORS-safelisted
    # headers, and as such should not include any user identification or
    # privacy sensitive information.
    kDeviceMemory_DEPRECATED = 0,
    kDpr_DEPRECATED = 1,
    kResourceWidth_DEPRECATED = 2,
    kViewportWidth_DEPRECATED = 3,
    kRtt_DEPRECATED = 4,
    kDownlink_DEPRECATED = 5,
    kEct_DEPRECATED = 6,
    # kLang = 7, Removed in M96
    kUA = 8,
    kUAArch = 9,
    kUAPlatform = 10,
    kUAModel = 11,
    kUAMobile = 12,
    # Sec-CH-UA-Full-Version is soon to be deprecated,
    # prefer Sec-CH-UA-Full-Version-List instead.
    kUAFullVersion = 13,
    kUAPlatformVersion = 14,
    kPrefersColorScheme = 15,
    kUABitness = 16,
    # A client hint which, if set, signifies to the origin that the User-Agent
    # header contains the reduced user agent string.
    kUAReduced = 17,
    kViewportHeight = 18,
    kDeviceMemory = 19,  # The `sec-ch-` variant of kDeviceMemory_DEPRECATED
    kDpr = 20,  # The `sec-ch-` variant of kDpr_DEPRECATED
    kResourceWidth = 21,  # The `sec-ch-` variant of kResourceWidth_DEPRECATED
    kViewportWidth = 22,  # The `sec-ch-` variant of kViewportWidth_DEPRECATED
    # A new client hint to deprecate `sec-ch-ua-full-version`
    kUAFullVersionList = 23,
    # A client hint which, if set, signifies to the origin that the User-Agent
    # header contains the full user agent string.
    kFullUserAgent = 24,
    kUAWoW64 = 25,
    # A client hint which, if set, signifies to the origin that the client
    # supports the Partitioned cookie attribute.
    kPartitionedCookies = 26,
    # Indicates the client wants to minimize data transfer if set to 'on'.
    kSaveData = 27,

    # Warning: Before adding a new client hint, read the warning at the top.


class WebEffectiveConnectionType(str, Enum):
    kTypeUnknown = '4g'
    kTypeOffline = '4g'
    kTypeSlow2G = 'slow-2g'
    kType2G = '2g'
    kType3G = '3g'
    kType4G = '4g'


@unique
class WebConnectionType(str, Enum):
    CELLULAR = 'cellular'
    BLUETOOTH = 'bluetooth'
    ETHERNET = 'ethernet'
    WIFI = 'wifi'
    WIMAX = 'wimax'
    OTHER = 'other'
    NONE = 'none'
    UNKNOWN = 'unknown'


@unique
class Platform(str, Enum):
    LINUX_ARMV8L = "Linux armv8l"
    LINUX_ARMV7L = "Linux armv7l"
    LINUX_ARMV6L = "Linux armv6l"
    LINUX_AARCH64 = "Linux aarch64"
    LINUX_X86_64 = "Linux x86_64"
    LINUX_I686 = "Linux i686"
    MACINTEL = "MacIntel"
    WIN32 = "Win32"
    WIN64 = "Win64"
    WINCE = "WinCE"
    SUNOS = "SunOS"
    IPHONE = "iPhone"
    IPOD = "iPod"
    IPAD = "iPad"


# @unique
# class PermissionType(int, Enum):
#     COOKIES = 0,
#     IMAGES = 1,  # 1
#     JAVASCRIPT = 2,  # 2
#
#     # This setting governs both popups and unwanted redirects like tab-unders and
#     # framebusting.
#     # TODO(csharrison): Consider renaming it to POPUPS_AND_REDIRECTS, but it
#     # might not be worth the trouble.
#     POPUPS = 3,  # 3
#
#     GEOLOCATION = 4,  # 4
#     NOTIFICATIONS = 5,  # 5
#     AUTO_SELECT_CERTIFICATE = 6,  # 6
#     MIXEDSCRIPT = 7,  # 7
#     MEDIASTREAM_MIC = 8,  # 8
#     MEDIASTREAM_CAMERA = 9,  # 9
#     PROTOCOL_HANDLERS = 10,  # 10
#     PPAPI_BROKER = 11,  # 11
#     AUTOMATIC_DOWNLOADS = 12,  # 12
#     MIDI_SYSEX = 13,  # 13
#     SSL_CERT_DECISIONS = 14,  # 14
#     PROTECTED_MEDIA_IDENTIFIER = 15,  # 15
#     APP_BANNER = 16,  # 16
#     SITE_ENGAGEMENT = 17,  # 17
#     DURABLE_STORAGE = 18,  # 18
#     USB_CHOOSER_DATA = 19,  # 19
#     BLUETOOTH_GUARD = 20,  # 20
#     BACKGROUND_SYNC = 21,  # 21
#     AUTOPLAY = 22,  # 22
#     IMPORTANT_SITE_INFO = 23,  # 23
#     PERMISSION_AUTOBLOCKER_DATA = 24,  # 24
#     ADS = 25,  # 25
#
#     # Website setting which stores metadata for the subresource filter to aid in
#     # decisions for whether or not to show the UI.
#     ADS_DATA = 26,  # 26
#
#     # This is special-cased in the permissions layer to always allow, and as
#     # such doesn't have associated prefs data.
#     MIDI = 27,  # 27
#
#     # This content setting type is for caching password protection service's
#     # verdicts of each origin.
#     PASSWORD_PROTECTION = 28,  # 28
#
#     # Website setting which stores engagement data for media related to a
#     # specific origin.
#     MEDIA_ENGAGEMENT = 29,  # 29
#
#     # Content setting which stores whether or not the site can play audible
#     # sound. This will not block playback but instead the user will not hear it.
#     SOUND = 30,  # 30
#
#     # Website setting which stores the list of client hints that the origin
#     # requested the browser to remember. The browser is expected to send all
#     # client hints in the HTTP request headers for every resource requested
#     # from that origin.
#     CLIENT_HINTS = 31,  # 31
#
#     # Generic Sensor API covering ambient-light-sensor, accelerometer, gyroscope
#     # and magnetometer are all mapped to a single content_settings_type.
#     # Setting for the Generic Sensor API covering ambient-light-sensor,
#     # accelerometer, gyroscope and magnetometer. These are all mapped to a single
#     # ContentSettingsType.
#     SENSORS = 32,  # 32
#
#     # Content setting which stores whether or not the user has granted the site
#     # permission to respond to accessibility events, which can be used to
#     # provide a custom accessibility experience. Requires explicit user consent
#     # because some users may not want sites to know they're using assistive
#     # technology.
#     ACCESSIBILITY_EVENTS = 33,  # 33
#
#     # Used to store whether to allow a website to install a payment handler.
#     PAYMENT_HANDLER = 34,  # 34
#
#     # Content setting which stores whether to allow sites to ask for permission
#     # to access USB devices. If this is allowed specific device permissions are
#     # stored under USB_CHOOSER_DATA.
#     USB_GUARD = 35,  # 35
#
#     # Nothing is stored in this setting at present. Please refer to
#     # BackgroundFetchPermissionContext for details on how this permission
#     # is ascertained.
#     BACKGROUND_FETCH = 36,  # 36
#
#     # Website setting which stores the amount of times the user has dismissed
#     # intent picker UI without explicitly choosing an option.
#     INTENT_PICKER_DISPLAY = 37,  # 37
#
#     # Used to store whether to allow a website to detect user active/idle state.
#     IDLE_DETECTION = 38,  # 38
#
#     # Setting for enabling auto-select of all screens for getDisplayMediaSet.
#     GET_DISPLAY_MEDIA_SET_SELECT_ALL_SCREENS = 39,  # 39
#
#     # Content settings for access to serial ports. The "guard" content setting
#     # stores whether to allow sites to ask for permission to access a port. The
#     # permissions granted to access particular ports are stored in the "chooser
#     # data" website setting.
#     SERIAL_GUARD = 40,  # 40
#     SERIAL_CHOOSER_DATA = 41,  # 41
#
#     # Nothing is stored in this setting at present. Please refer to
#     # PeriodicBackgroundSyncPermissionContext for details on how this permission
#     # is ascertained.
#     # This content setting is not registered because it does not require access
#     # to any existing providers.
#     PERIODIC_BACKGROUND_SYNC = 42,  # 42
#
#     # Content setting which stores whether to allow sites to ask for permission
#     # to do Bluetooth scanning.
#     BLUETOOTH_SCANNING = 43,  # 43
#
#     # Content settings for access to HID devices. The "guard" content setting
#     # stores whether to allow sites to ask for permission to access a device. The
#     # permissions granted to access particular devices are stored in the "chooser
#     # data" website setting.
#     HID_GUARD = 44,  # 44
#     HID_CHOOSER_DATA = 45,  # 45
#
#     # Wake Lock API, which has two lock types: screen and system locks.
#     # Currently, screen locks do not need any additional permission, and system
#     # locks are always denied while the right UI is worked out.
#     WAKE_LOCK_SCREEN = 46,  # 46
#     WAKE_LOCK_SYSTEM = 47,  # 47
#
#     # Legacy SameSite cookie behavior. This disables SameSite=Lax-by-default,
#     # SameSite=None requires Secure, and Schemeful Same-Site, forcing the
#     # legacy behavior wherein 1) cookies that don't specify SameSite are treated
#     # as SameSite=None, 2) SameSite=None cookies are not required to be Secure,
#     # and 3) schemeful same-site is not active.
#     #
#     # This will also be used to revert to legacy behavior when future changes
#     # in cookie handling are introduced.
#     LEGACY_COOKIE_ACCESS = 48,  # 48
#
#     # Content settings which stores whether to allow sites to ask for permission
#     # to save changes to an original file selected by the user through the
#     # File System Access API.
#     FILE_SYSTEM_WRITE_GUARD = 49,  # 49
#
#     # Content settings for installed web apps that browsing history may be
#     # inferred from e.g. last update check timestamp.
#     INSTALLED_WEB_APP_METADATA = 50,  # 50
#
#     # Used to store whether to allow a website to exchange data with NFC devices.
#     NFC = 51,  # 51
#
#     # Website setting to store permissions granted to access particular Bluetooth
#     # devices.
#     BLUETOOTH_CHOOSER_DATA = 52,  # 52
#
#     # Full access to the system clipboard (sanitized read without user gesture,
#     # and unsanitized read and write with user gesture).
#     # TODO(https:#crbug.com/1027225): Move CLIPBOARD_READ_WRITE uses to be
#     # ordered in the same order as listed in the enum.
#     CLIPBOARD_READ_WRITE = 53,  # 53
#
#     # This is special-cased in the permissions layer to always allow, and as
#     # such doesn't have associated prefs data.
#     # TODO(https:#crbug.com/1027225): Move CLIPBOARD_SANITIZED_WRITE uses to be
#     # ordered in the same order as listed in the enum.
#     CLIPBOARD_SANITIZED_WRITE = 54,  # 54
#
#     # This content setting type is for caching safe browsing real time url
#     # check's verdicts of each origin.
#     SAFE_BROWSING_URL_CHECK_DATA = 55,  # 55
#
#     # Used to store whether a site is allowed to request AR or VR sessions with
#     # the WebXr Device API.
#     VR = 56,  # 56
#     AR = 57,  # 57
#
#     # Content setting which stores whether to allow site to open and read files
#     # and directories selected through the File System Access API.
#     FILE_SYSTEM_READ_GUARD = 58,  # 58
#
#     # Access to first party storage in a third-party context. Exceptions are
#     # scoped to the combination of requesting/top-level origin, and are managed
#     # through the Storage Access API. For the time being, this content setting
#     # exists in parallel to third-party cookie rules stored in COOKIES.
#     # TODO(https:#crbug.com/989663): Reconcile the two.
#     STORAGE_ACCESS = 59,  # 59
#
#     # Content setting which stores whether to allow a site to control camera
#     # movements. It does not give access to camera.
#     CAMERA_PAN_TILT_ZOOM = 60,  # 60
#
#     # Content setting for Screen Enumeration and Window Placement functionality.
#     # Permits access to information about the screens, like size and position.
#     # Permits creating and placing windows across the set of connected screens.
#     WINDOW_PLACEMENT = 61,  # 61
#
#     # Stores whether to allow insecure websites to make private network requests.
#     # See also: https:#wicg.github.io/cors-rfc1918
#     # Set through enterprise policies only.
#     INSECURE_PRIVATE_NETWORK = 62,  # 62
#
#     # Content setting which stores whether or not a site can access low-level
#     # locally installed font data using the Local Fonts Access API.
#     LOCAL_FONTS = 63,  # 63
#
#     # Stores per-origin state for permission auto-revocation (for all permission
#     # types).
#     PERMISSION_AUTOREVOCATION_DATA = 64,  # 64
#
#     # Stores per-origin state of the most recently selected directory for the use
#     # by the File System Access API.
#     FILE_SYSTEM_LAST_PICKED_DIRECTORY = 65,  # 65
#
#     # Controls access to the getDisplayMedia API when {preferCurrentTab: true}
#     # is specified.
#     # TODO(crbug.com/1150788): Also apply this when getDisplayMedia() is called
#     # without specifying {preferCurrentTab: true}.
#     # No values are stored for this type, this is solely needed to be able to
#     # register the PermissionContext.
#     DISPLAY_CAPTURE = 66,  # 66
#
#     # Website setting to store permissions metadata granted to paths on the local
#     # file system via the File System Access API. |FILE_SYSTEM_WRITE_GUARD| is
#     # the corresponding "guard" setting.
#     FILE_SYSTEM_ACCESS_CHOOSER_DATA = 67,  # 67
#
#     # Stores a grant for the browser to intermediate or allow without
#     # restriction sharing of identity information by an identity provider to
#     # specified relying parties. The setting is associated with the identity
#     # provider's origin.
#     # This is managed by WebID.
#     FEDERATED_IDENTITY_SHARING = 68,  # 68
#
#     # Stores a grant that allows a relying party to send a request for identity
#     # information to specified identity providers, potentially through any
#     # anti-tracking measures that would otherwise prevent it. This setting is
#     # associated with the relying party's origin.
#     FEDERATED_IDENTITY_REQUEST = 69,  # 69
#
#     # Whether to use the v8 optimized JIT for running JavaScript on the page.
#     JAVASCRIPT_JIT = 70,  # 70
#
#     # Content setting which stores user decisions to allow loading a site over
#     # HTTP. Entries are added by hostname when a user bypasses the HTTPS-First
#     # Mode interstitial warning when a site does not support HTTPS. Allowed hosts
#     # are exact hostname matches -- subdomains of a host on the allowlist must be
#     # separately allowlisted.
#     HTTP_ALLOWED = 71,  # 71
#
#     # Stores metadata related to form fill, such as e.g. whether user data was
#     # autofilled on a specific website.
#     FORMFILL_METADATA = 72,  # 72
#
#     # Setting to indicate that there is an active federated sign-in session
#     # between a specified relying party and a specified identity provider for
#     # a specified account. When this is present it allows access to session
#     # management capabilities between the sites. This setting is associated
#     # with the relying party's origin.
#     FEDERATED_IDENTITY_ACTIVE_SESSION = 73,  # 73
#
#     # Setting to indicate whether Chrome should automatically apply darkening to
#     # web content.
#     AUTO_DARK_WEB_CONTENT = 74,  # 74
#
#     # Setting to indicate whether Chrome should request the desktop view of a
#     # site instead of the mobile one.
#     REQUEST_DESKTOP_SITE = 75,  # 75
#
#     # Setting to indicate whether browser should allow signing into a website via
#     # the browser FedCM API.
#     FEDERATED_IDENTITY_API = 76,  # 76
#
#     NUM_TYPES = 77,  # 77


class CookieSameSite(int, Enum):
    UNSPECIFIED = -1
    NO_RESTRICTION = 0
    LAX_MODE = 1
    STRICT_MODE = 2
    kMaxValue = STRICT_MODE
