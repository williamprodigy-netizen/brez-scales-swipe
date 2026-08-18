#!/usr/bin/env python3
"""Build the Brez Scales swipe site. Run: python3 build_site.py"""
import sys, os, glob, subprocess
sys.path.insert(0, os.path.expanduser("~/scripts/_swipe_builder"))
from swipebuild import build

REPO = os.path.dirname(os.path.abspath(__file__))
PKG = os.path.expanduser("~/Downloads/Swipes/BREZ_SCALES_Swipe")


def _probe(p):
    try:
        return int(float(subprocess.run(
            ["ffprobe", "-v", "error", "-show_entries", "format=duration",
             "-of", "csv=p=0", p], capture_output=True, text=True, timeout=60).stdout.strip()))
    except Exception:
        return 0


def video_library():
    rows = []
    for p in sorted(glob.glob(os.path.join(PKG, "Recording/**/*.mp4"), recursive=True)):
        mb = os.path.getsize(p) / 1e6
        rows.append((os.path.basename(p), _probe(p),
                     f"{mb/1000:.1f} GB" if mb >= 1000 else f"{mb:.0f} MB",
                     ROLES.get(os.path.basename(p), "")))
    return rows


ROLES = {'BrezScales_MainVSL.mp4': 'Main-page video, served by ConverteAI. Short.'}

CONFIG = {
 "SITE": "Brez Scales — Elite Round Table",
 "CREATOR": "Brez Scales",
 "ADS_KEY": "brezscales",
 "FUNNEL_IDS": ["F068"],
 "CAPTURED": "18 August 2026",
 "REPO": REPO,
 "PACKAGE": "~/Downloads/Swipes/BREZ_SCALES_Swipe",
 "BLURB": "Freelance &ldquo;brand scaling&rdquo; taught through a free front end that is openly "
          "<b>de-priced from a $5,000 course</b>, then routed into the Elite Round Table application.",
 "PAGES": [("index.html","Overview"),("analysis.html","Analysis"),
              ("transcripts.html","Transcripts"),("videos.html","Video library")],
 "STATS": [("Front end","Free system"),("Anchor","Was part of a <b>$5,000</b> course"),
           ("Back end","Elite Round Table (ERT)"),("Main video","2m 10s"),("Words","515"),
           ("Speed promise","Text and call in <b>2 minutes</b>"),
           ("Stack","ClickFunnels + Typeform + Hyros"),("Dead URLs","2 of 6")],
 "OFFER": [("Hook","&ldquo;This used to be part of my <b>$5,000 course</b>. Now you can learn it for free.&rdquo;"),
   ("Objection pre-empted","The page's own H2 is <b>&ldquo;How Is This Free?&rdquo;</b>"),
   ("Skill sold","Freelance brand scaling &mdash; &ldquo;no product to build, work from anywhere, AI helps you&rdquo;"),
   ("Back end","<b>Elite Round Table</b> on a separate domain, brezscales.co"),
   ("Speed promise","&ldquo;Expect to receive a text and a call in the <b>next 2 minutes</b>&rdquo;"),
   ("Path","Free system &rarr; application &rarr; ERT direct &rarr; pre-call &rarr; booked call"),
   ("Price","<b>Never stated</b> for ERT. The only number in the funnel is the $5,000 anchor")],
 "FINDINGS": [
  ("The price anchor is the hook, and it is a price he is no longer charging",
   "<i>&ldquo;This used to be part of my <b>$5,000 course</b>. Now you can learn it for free.&rdquo;</i> "
   "A free offer normally reads as worth nothing. Attaching it to a real, abandoned price gives "
   "the free thing a receipt. <b>He never has to defend the $5,000 &mdash; he is not charging it.</b> "
   "It is the cleanest free-lead-magnet framing in this file."),
  ("He answers &ldquo;what's the catch&rdquo; as a page section",
   "The second H2 is literally <b>&ldquo;How Is This Free?&rdquo;</b>. The objection that a "
   "$5,000-anchored freebie creates is the very next thing the page handles. Most funnels create "
   "that suspicion and leave it running."),
  ("A two-minute callback promise, in writing",
   "The application confirmation reads <i>&ldquo;Congrats for applying. Expect to receive a text "
   "and a call in the <b>next 2 minutes</b>&rdquo;</i>. That is a commitment the sales team must "
   "then hit, and it makes the speed-to-lead standard visible to the lead. <span class=\"tag good\">worth stealing</span>"),
  ("Forced consumption stated as an instruction, not enforced by the player",
   "The ERT page says <b>&ldquo;do NOT apply before watching the video below&rdquo;</b>. No locked "
   "player, no timer &mdash; just an instruction. Cheaper than Brook Hiddink's enforced version, "
   "and it filters on compliance rather than patience."),
  ("Two of six funnel URLs are dead",
   "<code>/en/free-training-org</code> and the LeadConnector booking widget both return <b>404</b>. "
   "The organic training path and one booking route are broken as of 18 August. Either mid-migration, "
   "or leaking traffic."),
 ],
 "FUNNEL": [
  ("Main page","joinbrezscales.com",'<span class="tag good">the hook</span> &ldquo;Used to be part of my $5,000 course.&rdquo; ConverteAI video, 2m10s. Meta, GTM, GA, Clarity, Hyros.'),
  ("Free training (organic)","/en/free-training-org",'<span class="tag bad">404</span> Dead as of 18 Aug.'),
  ("Application","/en/application","&ldquo;Expect a text and a call in the next 2 minutes.&rdquo; Income disclaimer."),
  ("ERT direct","brezscales.co/ert-direct","Elite Round Table. &ldquo;Do NOT apply before watching.&rdquo; ClickFunnels + Typeform + Intercom + Hyros."),
  ("Booking widget","api.leadconnectorhq.com/widget/booking/…",'<span class="tag bad">404</span> Dead.'),
  ("Pre-call","brezscales.co/precall--2153c","Step 1 watch in full, Step 2 FAQ videos. 3 member-story videos."),
 ],
 "TRANSCRIPT_GROUPS": [("Main page video",[os.path.join(PKG,"Transcript/transcript.md")])],
 "SLIDE_PAGES": [],
 "ANALYSIS": """
<div class="note"><b>The hook is the whole lesson.</b> &ldquo;This used to be part of my $5,000
course. Now you can learn it for free.&rdquo; It solves the hardest problem a free offer has
&mdash; that free things are assumed worthless &mdash; with a price he no longer charges and
therefore never has to defend.</div>

<h2 class="sec">Why the de-priced anchor beats a stacked value</h2>
<div class="tablewrap"><table>
<tr><th>Approach</th><th>What the prospect thinks</th></tr>
<tr><td>&ldquo;A $16,967 value, yours free&rdquo;</td><td>Invented number. Nobody ever paid that.</td></tr>
<tr><td>&ldquo;Normally $997, free today&rdquo;</td><td>Then why is it free? What's wrong with it?</td></tr>
<tr><td><b>&ldquo;Used to be part of my $5,000 course. Now it's free.&rdquo;</b></td><td><b>Real price, real past, and he pre-empts the catch on the next line.</b></td></tr>
</table></div>
<p style="margin-top:12px"><span class="tag">READ</span> Our masterclass is free and unpriced.
There is a true version of this sentence available to us &mdash; parts of the class genuinely were
paid curriculum &mdash; and we have never said it.</p>

<h2 class="sec">Two brands, one funnel</h2>
<p>The front end is <b>joinbrezscales.com</b> (Meta Pixel, GTM, GA, Clarity, Hyros). The back end is
<b>brezscales.co</b> running <b>ClickFunnels</b> with Typeform, Intercom and New Relic. Different
domain, different stack, different tracking. The free-education brand and the sales machine are
deliberately separated &mdash; the same split Viral Coach makes between its main page and its
application page.</p>

<h2 class="sec">The funnel is partly broken right now</h2>
<p><span class="tag">EVIDENCE</span> Two of six registered URLs return 404: the organic free-training
page and the LeadConnector booking widget. Captured 18 August 2026. If ads or bio links still point
at either, that is live lost traffic. Recorded as observed, not diagnosed &mdash; we cannot see
their ad destinations from here.</p>

<h2 class="sec">What is missing</h2>
<ul><li><b>No ERT price</b> anywhere in the funnel.</li>
<li><b>The main video is only 2m10s</b> &mdash; this is a hook, not a full VSL. The substantive
pitch is likely inside the ERT pages or the call itself.</li>
<li><b>No emails</b> &mdash; opt-in never submitted.</li>
<li><b>The 3 member-story videos are identified but not pulled</b> (YouTube rate-limited at capture time).</li></ul>
""",
}
CONFIG["VIDEOS"] = video_library()

if __name__ == "__main__":
    build(CONFIG)
