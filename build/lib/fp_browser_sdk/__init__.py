from .fp_browser_settings import FPBrowserSettings
from ext.basic import Basic
from ext.navigator import Navigator
from ext.client_hints import ClientHints
from ext.screen import Screen
from ext.header import Cookie, Header
from ext.webrtc import Webrtc
from ext.battery import Battery
from ext.fingerprint_offset import FingerprintOffset
from ext.document import Document, VideoSupport, DocumetMatch
from ext.media import Media
from ext.network import Network
from ext.device_motion import DeviceMotion
from ext.device_orientation import DeviceOrientation
from ext.speech_synthesis_voice import SpeechSynthesisVoice, SpeechSynthesisVoiceItem
from ext.browser_enum import TLSVersion, Platform, CompatMode, \
    SpeechSynthesisVoiceAppendMode, PerformanceNavigationType, MaxTouchPoint, \
    WebConnectionType, WebEffectiveConnectionType, ScreenOrientationType, ScreenColorDepth, CookieSameSite, MatchType
from ext.inject_js import InjectJS
from ext.exception import MotionErrorException
import json
import random
import os
from fp_browser.fp_browser.data.motion import motion_result
from ext.performance import Performance, PerformanceMatch
from .ext.permission_types import PermissionType, get_permission_type


class ConfigConvertSetting(object):
    def __init__(self, key, config: dict = None, config_path: str = None, browser_version: int = 102):
        if config_path is not None:
            config = self.get_config(file=config_path)

        config['font_list'] = json.loads(config['font_list'])
        config['userAgentData'] = json.loads(config['userAgentData'])
        config['devices'] = json.loads(config['devices'])
        config['languages'] = json.loads(config['languages'])
        config['support_video'] = json.loads(config['support_video'])
        config['voice_list'] = json.loads(config['voice_list'])

        self.config = config
        self.browser_version = browser_version
        self.settings = FPBrowserSettings(key=key)
        pass

    def get_config(self, file):
        """
        读取 js 内容
        """
        return json.loads(self.get_file_context(file))

    def get_file_context(self, file):
        """
        读取文件内容
        """
        with open(file) as f:
            context = f.read()
            f.close()
            return context

    def _get_permission_type(self, permission_type: PermissionType):
        """
        获得权限类型
        """
        return get_permission_type(permission_type=permission_type, version=self.browser_version)

    def set_basic(self, version_info_number):
        """
        basic
        """
        load_js = ''

        basic = Basic() \
            .set_global_disable_settings(False) \
            .set_disable_window(False) \
            .set_info_number(version_info_number) \
            .set_time_zone("Asia/Shanghai") \
            .set_init_history_length(random.randint(1, 20)) \
            .set_inject_js(InjectJS().append_load_event(load_js)) \
            .append_reject_permission(self._get_permission_type(permission_type=PermissionType.NOTIFICATIONS)) \
            .append_reject_permission(self._get_permission_type(permission_type=PermissionType.GEOLOCATION)) \
            .append_reject_permission(self._get_permission_type(permission_type=PermissionType.CLIPBOARD_READ_WRITE)) \
            .set_webgl_vendor(self.config['webgl_vendor']) \
            .set_webgl_renderer(self.config['webgl_renderer']) \
            .set_memory_info_limit_js(self.config['jsHeapSizeLimit']) \
            .set_disable_alert(True) \
            .set_disable_window_open(True) \
            .set_confirm(True) \
            .set_tls_min_ver(TLSVersion.TLS_1_2) \
            .set_tls_max_ver(TLSVersion.TLS_1_3)

        if len(self.config['font_list']) > 0:
            for font in self.config['font_list']:
                basic.append_font(font)

        if len(self.config['devices']) > 0:
            for device in self.config['devices']:
                media = Media() \
                    .set_label(device['label']) \
                    .set_kind(Media.str_to_kind_type(device['kind'])) \
                    .set_device_id(device['deviceId']) \
                    .set_groupId(device['groupId'])

                basic.append_media(media)

        self.settings.add_module(basic)
        return self

    def set_navigator(self, url_match: dict, version_info_number: str):
        """
        navigator
        """
        navigator = Navigator() \
            .set_user_agent(self.config['userAgent']) \
            .set_user_agent_auto_match(True) \
            .set_platform(Platform(self.config['platform'])) \
            .set_max_touch_points(MaxTouchPoint.MOBILE) \
            .set_hardware_concurrency(self.config['hardwareConcurrency']) \
            .set_device_memory(self.config['deviceMemory']) \
            .set_performance_type(PerformanceNavigationType.NAVIGATE) \
            .set_enable_plugin(False) \
            .set_online(True) \
            .set_java_enabled(self.config['javaEnabled'] == 1) \
            .set_pdf_viewer_enabled(self.config['pdfViewerEnabled'] == 1) \
            .set_bluetooth_availability(True) \
            .set_language(self.config['language']) \
            .set_languages(','.join(self.config['languages'])) \
            .set_webdriver_status(False)

        # 如果有设置版本，并且主版本号是大于等于 101，则强制设置 ua 的小版本号是 .0.0.0
        if version_info_number and len(version_info_number) > 0:
            version_info_number_result = version_info_number.split('.')

            if version_info_number_result and len(version_info_number_result) == 4:
                major_version_number = int(version_info_number_result[0])

                if major_version_number >= 101:
                    navigator.set_reduced_major_in_minor_version_number(True)

        self.settings.add_module(navigator)

        performance = Performance() \
            .append_match(PerformanceMatch() \
                          .set_match_type(MatchType.FULL) \
                          .set_target_url(url_match['target-url']) \
                          .set_navigation_redirect_count(0) \
                          .set_navigation_type(PerformanceNavigationType.NAVIGATE)
                          )

        self.settings.add_module(performance)

        return self

    def set_document(self, url_match: dict):
        """
        document
        """
        document = Document() \
            .set_is_trusted(True) \
            .set_charset('UTF-8') \
            .set_lastModified(url_match['match-tlm']) \
            .set_compat_mode(CompatMode(self.config['compatMode']))

        match = DocumetMatch() \
            .set_match_type(MatchType.FULL) \
            .set_target_url(url_match['target-url']) \
            .set_title(url_match['match-title']) \
            .set_document_referrer(url_match['match-referrer']) \
            .set_header_referrer("") \
            .set_current_url(url_match['match-url'])

        document.append_match_list(match)

        if len(self.config['support_video']) > 0:
            for (index, value) in enumerate(self.config['support_video']):
                if index == 0 and value:
                    document.append_video_support_mime_types(VideoSupport().set_type('video/ogg; codecs="theora"'))
                elif index == 1 and value:
                    document.append_video_support_mime_types(VideoSupport().set_type('video/mp4; codecs="avc1.42E01E"'))
                elif index == 2 and value:
                    document.append_video_support_mime_types(VideoSupport().set_type('video/webm; codecs="vp9"'))
                    document.append_video_support_mime_types(
                        VideoSupport().set_type('video/webm; codecs="vp8, vorbis"'))
                elif index == 3 and value:
                    document.append_video_support_mime_types(
                        VideoSupport().set_type('application/x-mpegURL; codecs="avc1.42E01E"'))

        self.settings.add_module(document)
        return self

    def set_screen(self):
        """
        screen
        """
        screen = Screen() \
            .append_media_matchs("color-gamut", "srgb") \
            .append_media_matchs("forced-colors", "none") \
            .set_width(self.config['width']) \
            .set_height(self.config['height']) \
            .set_avail_width(self.config['avail_width']) \
            .set_avail_height(self.config['avail_height']) \
            .set_avail_top(0) \
            .set_avail_left(0) \
            .set_device_pixel_ratio(self.config['devicePixelRatio']) \
            .set_rect_width(self.config['outer_size_width']) \
            .set_rect_height(self.config['outer_size_height']) \
            .set_orientation(ScreenOrientationType.PORTRAIT_PRIMARY) \
            .set_color_depth(ScreenColorDepth(self.config['colorDepth']))

        if self.config['color_gamut']:
            screen.append_media_matchs("color-gamut", self.config['color_gamut'])

        if self.config['forced_color']:
            screen.append_media_matchs("forced-colors", self.config['forced_color'])

        if self.config['hdr_mode']:
            screen.append_media_matchs("dynamic-range", self.config['hdr_mode'])

        if self.config['contrast_preference']:
            screen.append_media_matchs("prefers-contrast", self.config['contrast_preference'])

        if self.config['colors_inverted']:
            screen.append_media_matchs("inverted-colors", self.config['colors_inverted'])

        self.settings.add_module(screen)
        return self

    def set_clientHints(self, disable_client_hints):
        """
        clientHints
        """
        clientHints = ClientHints() \
            .set_disable(disable_client_hints)

        self.settings.add_module(clientHints)
        return self

    def set_header(self, cookie: list, domain: str):
        """
        header
        """
        return self

    def random_local_ip(self, connection_type: WebConnectionType):
        """
        根据网络随机一个局域网 ip
        """
        # 如果是非 wifi，则用 10 的网段
        if connection_type != WebConnectionType.WIFI:
            return '10.' + str(random.randint(0, 30)) + '.' + str(random.randint(1, 254)) + '.' + str(
                random.randint(1, 254))

        prefix = [
            '192.168.0',
            '192.168.1',
            '172.16.0',
            '172.16.1',
        ]

        return random.choice(prefix) + '.' + str(random.randint(0, 254))

    def set_webrtc(self, real_ip: str, connection_type: WebConnectionType):
        """
        webrtc
        """

        webrtc = Webrtc() \
            .set_privite_ip(self.random_local_ip(connection_type)) \
            .set_public_ip(real_ip)

        self.settings.add_module(webrtc)
        return self

    def set_fingerprint_offset(self):
        """
        fingerprint_offset
        """
        fingerprint_offset = FingerprintOffset() \
            .auto_audio_offset() \
            .auto_canvas_offset() \
            .auto_webgl_offset()

        self.settings.add_module(fingerprint_offset)
        return self

    def set_speech_synthesis_voice(self):
        """
        fingerprint_offset
        """
        speech_synthesis_voice = SpeechSynthesisVoice()

        if len(self.config['voice_list']) > 0:
            speech_synthesis_voice.set_force_override(True) \
                .set_append_mode(SpeechSynthesisVoiceAppendMode.PUSH)
            for voice in self.config['voice_list']:
                item = SpeechSynthesisVoiceItem() \
                    .set_name(voice['name']) \
                    .set_lang(voice['lang']) \
                    .set_is_local_service(voice['localService'])

                speech_synthesis_voice.append_list(item)
        else:
            # 如果没有，则强制关闭掉
            speech_synthesis_voice.set_disable(True)

        self.settings.add_module(speech_synthesis_voice)
        return self

    def set_network(self, connection_type: WebConnectionType, effective_type: WebEffectiveConnectionType):
        """
        network
        """
        network = Network().generate_connect_type(connection_type=connection_type, effective_type=effective_type)

        self.settings.add_module(network)
        return self

    def set_battery(self):
        """
        network
        """
        network = Battery().generate()

        self.settings.add_module(network)
        return self

    def set_motion(self):
        """
        重力感应
        """
        data = None
        if motion_result and len(motion_result) > 0:
            while True:
                data = random.choice(motion_result)

                if data and 'x1' in data \
                        and 'y1' in data \
                        and 'z1' in data \
                        and 'x2' in data \
                        and 'y2' in data \
                        and 'z2' in data \
                        and 'alpha1' in data \
                        and 'beta1' in data \
                        and 'gamma1' in data \
                        and 'alpha2' in data \
                        and 'beta2' in data \
                        and 'gamma2' in data \
                        and 'is_absolute' in data:
                    break

        if data is None:
            raise MotionErrorException()

        motion = DeviceMotion().set_x1(data['x1']) \
            .set_y1(data['y1']) \
            .set_z1(data['z1']) \
            .set_x2(data['x2']) \
            .set_y2(data['y2']) \
            .set_z2(data['z2']) \
            .set_alpha(data['alpha1']) \
            .set_beta(data['beta1']) \
            .set_gamma(data['gamma1'])

        orientation = DeviceOrientation().set_alpha(data['alpha2']) \
            .set_beta(data['beta2']) \
            .set_gamma(data['gamma2']) \
            .set_absolute(False)

        self.settings.add_module(motion)
        self.settings.add_module(orientation)
        return self

    def handle(self, cookie: list, cookie_domain: str, real_ip: str, connection_type: WebConnectionType,
               effective_type: WebEffectiveConnectionType, version_info_number, url_match: dict,
               disable_client_hints=True):
        """
        解析参数
        """
        self.set_basic(version_info_number) \
            .set_navigator(url_match=url_match, version_info_number=version_info_number) \
            .set_document(url_match=url_match) \
            .set_screen() \
            .set_header(cookie=cookie, domain=cookie_domain) \
            .set_fingerprint_offset() \
            .set_clientHints(disable_client_hints) \
            .set_webrtc(real_ip=real_ip, connection_type=connection_type) \
            .set_speech_synthesis_voice() \
            .set_battery() \
            .set_motion() \
            .set_network(connection_type=connection_type, effective_type=effective_type)

        return self.settings.parse()
