## 联系我
微信: @tyua07

![wechat](https://github.com/tyua07/FP-Browser-Detect/raw/master/docs/wechat.jpg)

## 项目介绍
浏览器属性注入参数 SDK

## 相关开源项目
* [FP-Browser-Public 浏览器底层动态注入](https://github.com/tyua07/FP-Browser-Public) 
* [FP-Browser-Detect 浏览器属性检测](https://github.com/tyua07/FP-Browser-Detect)
* [FP-Browser-SDK 浏览器属性注入参数 SDK](https://github.com/tyua07/FP-Browser-SDK)

## 示例代码

```
from fp_browser_sdk.fp_browser_settings import FPBrowserSettings
from fp_browser_sdk.ext.basic import Basic
from fp_browser_sdk.ext.navigator import Navigator
from fp_browser_sdk.ext.client_hints import ClientHints
from fp_browser_sdk.ext.screen import Screen
from fp_browser_sdk.ext.header import Cookie, Header
from fp_browser_sdk.ext.webrtc import Webrtc
from fp_browser_sdk.ext.geo import Geo
from fp_browser_sdk.ext.battery import Battery
from fp_browser_sdk.ext.fingerprint_offset import FingerprintOffset
from fp_browser_sdk.ext.document import Document, VideoSupport, Match
from fp_browser_sdk.ext.media import Media
from fp_browser_sdk.ext.device_orientation import DeviceOrientation
from fp_browser_sdk.ext.device_motion import DeviceMotion
from fp_browser_sdk.ext.network import Network
from fp_browser_sdk.ext.speech_synthesis_voice import SpeechSynthesisVoice, SpeechSynthesisVoiceItem
from fp_browser_sdk.ext.browser_enum import PermissionType, BaseEnum, TLSVersion, Platform, PrefersColor, \
    CompatMode, MatchType, SpeechSynthesisVoiceAppendMode, PerformanceNavigationType, DoNotTrackType, MaxTouchPoint, \
    ScreenColorDepth, ScreenOrientationType, MediaKind, WebEffectiveConnectionType, WebConnectionType
from fp_browser_sdk.ext.inject_js import InjectJS

settings = FPBrowserSettings(key="test")

basic = Basic() \
    .set_global_disable_settings(True) \
    .set_disable_window(False) \
    .set_time_zone("Asia/Beijing") \
    .set_init_history_length(12121) \
    .set_inject_js(InjectJS().append_load_event("alert('111223')")) \
    .append_allow_permission(PermissionType.GEOLOCATION) \
    .append_allow_permission(PermissionType.CLIPBOARD_READ_WRITE) \
    .append_reject_permission(PermissionType.NOTIFICATIONS) \
    .append_font("微软雅黑") \
    .set_product_name("Google Chromium") \
    .set_info_number("89.0.0.4389") \
    .set_webgl_vendor("Qualcomm") \
    .set_webgl_renderer("Adreno (TM) 630") \
    .set_memory_info_total_js(10000000) \
    .set_memory_info_used_js(10000000) \
    .set_memory_info_limit_js(1008000000) \
    .set_disable_alert(True) \
    .set_disable_window_open(True) \
    .set_confirm(True) \
    .append_media(Media().set_label(None).set_kind(MediaKind.AUDIO_INPUT).set_device_id('default').set_groupId(
    '88eb82896fee11289617b63418878ec6da61ea12a619705fd692aa4785225d14')) \
    .set_tls_min_ver(TLSVersion.TLS_1_2) \
    .set_tls_max_ver(TLSVersion.TLS_1_3)

navigator = Navigator() \
    .set_user_agent(
    'Mozilla/5.0 (Linux; Android 10; SM-G9600) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Mobile Safari/537.36') \
    .set_platform(Platform.LINUX_ARMV7L) \
    .set_max_touch_points(MaxTouchPoint.MOBILE) \
    .set_hardware_concurrency(6) \
    .set_device_memory(6) \
    .set_do_not_track(DoNotTrackType.UNSPECIFIED) \
    .set_performance_type(PerformanceNavigationType.BACK_FORWARD) \
    .set_enable_plugin(False) \
    .set_online(False) \
    .set_java_enabled(True) \
    .set_pdf_viewer_enabled(True) \
    .set_bluetooth_availability(False) \
    .set_language("zh") \
    .set_languages("zh,cn") \
    .set_webdriver_status(False)

clientHints = ClientHints() \
    .set_viewport_width(900) \
    .set_viewport_height(900) \
    .set_prefers_color(PrefersColor.DARK) \
    .set_platform_version("10.0.0") \
    .set_architecture("set_architecture") \
    .set_bitness("set_bitness") \
    .set_wow64(True) \
    .set_model('SM-G9600') \
    .set_disable(False)

screen = Screen() \
    .append_media_matchs("color-gamut", "srgb") \
    .append_media_matchs("forced-colors", "none") \
    .set_width(414) \
    .set_height(985) \
    .set_avail_width(414) \
    .set_avail_height(985) \
    .set_avail_top(0) \
    .set_avail_left(0) \
    .set_device_pixel_ratio(3.0) \
    .set_rect_width(414) \
    .set_rect_height(758) \
    .set_rect_scale_factor(2.75) \
    .set_orientation(ScreenOrientationType.PORTRAIT_PRIMARY) \
    .set_color_depth(ScreenColorDepth.ColorDepth_30)

header = Header() \
    .set_x_requested_with('com.xunmeng.pinduoduo') \
    .append_extra_json("key1", "value1") \
    .append_extra_json("key2", "value2") \
    .set_cookie_status(False)

webrtc = Webrtc() \
    .set_privite_ip("192.168.0.100") \
    .set_public_ip("8.8.8.8") \
    .set_host_name("sasasa")

fingerprint_offset = FingerprintOffset() \
    .auto_audio_offset() \
    .auto_canvas_offset() \
    .auto_webgl_offset()

geo = Geo() \
    .set_longitude("113.219875") \
    .set_latitude("23.401172") \
    .set_accuracy("14") \
    .set_altitude("13") \
    .set_altitude_accuracy("12") \
    .set_heading("11") \
    .set_speed(BaseEnum.NULL.value)

document = Document() \
    .set_global_match_target_url('so.com') \
    .set_global_match_title('最痛苦0-1!归化球员5分钟内乌龙+红牌 或无缘世界杯|红牌|世界杯|马里|西萨科_手机网易网') \
    .set_global_match_current_url('https://3g.163.com/sports/article/H3CC1DJ300058781.html') \
    .set_global_skip_current_url_header(True) \
    .set_global_match_referrer('https://m.baidu.com') \
    .append_match_list(Match()
                       .set_target_url("https://ly.so.com/") \
                       .set_match_break(True) \
                       .set_current_url("https://2g.163.com/") \
                       .set_referrer("https://m.baidu.com/1234") \
                       .set_title("love you") \
                       .set_match_type(MatchType.PATH)
                       ) \
    .set_is_trusted(True) \
    .append_video_support_mime_types(VideoSupport().set_type('video/test')) \
    .append_video_support_mime_types(VideoSupport().set_type('video/ogg; codecs="theora"')) \
    .set_compat_mode(CompatMode.CSS1COMPAT)

speech_synthesis_voice = SpeechSynthesisVoice() \
    .append_list(SpeechSynthesisVoiceItem().set_name('英语 美国').set_lang('en_US').set_is_local_service(True)) \
    .set_append_mode(SpeechSynthesisVoiceAppendMode.PUSH) \
    .set_force_override(True)

battery = Battery() \
    .set_level(98) \
    .set_charging_time(97) \
    .set_discharging_time(96) \
    .set_charging(True)

network = Network() \
    .set_effective_type(WebEffectiveConnectionType.kType3G) \
    .set_downlink(1.67) \
    .set_downlink_max(1) \
    .set_rtt(99) \
    .set_save_data(True) \
    .set_type(WebConnectionType.WIFI)

device_orientation = DeviceOrientation() \
    .set_alpha(0.0563243012168639, 0.1, 0.2) \
    .set_beta(1.1776552402780747, 0.1, 0.2) \
    .set_gamma(-0.027885421225340653, 0.1, 0.2) \
    .set_absolute(True)

device_motion = DeviceMotion() \
    .set_x1(0.0563243012168639, 0.1, 0.2) \
    .set_y1(1.1776552402780747, 0.1, 0.2) \
    .set_z1(-0.027885421225340653, 0.1, 0.2) \
    .set_x2(0.0563243012168639, 0.1, 0.2) \
    .set_y2(1.1776552402780747, 0.1, 0.2) \
    .set_z2(-0.027885421225340653, 0.1, 0.2) \
    .set_alpha(0.0563243012168639, 0.1, 0.2) \
    .set_beta(1.1776552402780747, 0.1, 0.2) \
    .set_gamma(-0.027885421225340653, 0.1, 0.2) \
    .set_interval(123)

settings.add_module(basic)
settings.add_module(navigator)
settings.add_module(clientHints)
settings.add_module(screen)
settings.add_module(header)
settings.add_module(webrtc)
settings.add_module(fingerprint_offset)
settings.add_module(geo)
settings.add_module(document)
settings.add_module(speech_synthesis_voice)
settings.add_module(battery)
settings.add_module(network)
settings.add_module(device_orientation)
settings.add_module(device_motion)

print(settings.parse())

```