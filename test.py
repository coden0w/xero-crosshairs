import os
from xml.dom import minidom

restore = """\
<?xml version="1.0" encoding="utf-8"?>\n
<crosshairs>
	<crosshair id="2000001" path="melee.dds" /> <!-- Plasma Sword -->
	<crosshair id="2000002" path="melee.dds" /> <!-- Counter Sword -->
	<crosshair id="2000003" path="melee.dds" /> <!-- Storm Bat -->
	<crosshair id="2000006" path="melee.dds" /> <!-- Spy Dagger -->
	<crosshair id="2000010" path="melee.dds" /> <!-- Twin Blades -->
	<crosshair id="2000013" path="melee.dds" /> <!-- Breaker -->
	<crosshair id="2000017" path="melee.dds" /> <!-- Sigma Blade -->
	<crosshair id="2000018" path="melee.dds" /> <!-- Katana -->
	<crosshair id="2000029" path="melee.dds" /> <!-- Exo Scythe -->
	<crosshair id="2000030" path="melee.dds" /> <!-- Iron Boots -->
	<crosshair id="2000036" path="melee.dds" /> <!-- Metallic Fist -->
	<crosshair id="2000063" path="melee.dds" /> <!-- Vital Shock -->
	<crosshair id="2010000" path="cross.dds" /> <!-- Submachine Gun -->
	<crosshair id="2010002" path="cross.dds" /> <!-- Revolver -->
	<crosshair id="2010004"> <!-- Semi Rifle -->
		<primary path="cross.dds" />
		<secondary path="zoom.dds" />
	</crosshair>
	<crosshair id="2020001" path="cross.dds" /> <!-- Heavy Machine Gun -->
	<crosshair id="2030001"> <!-- Rail Gun -->
		<primary path="circle2.dds" />
		<secondary path="zoom.dds" />
	</crosshair>
	<crosshair id="2030002"> <!-- Cannonade -->
		<primary path="circle3.dds" />
		<secondary path="zoom1.dds" />
	</crosshair>
	<crosshair id="2040001" path="stationary.dds" /> <!-- Sentry Gun -->
	<crosshair id="2050001" path="projectile.dds" /> <!-- Mine Gun -->
	<crosshair id="2060001" path="circle.dds" /> <!-- Mind Energy -->
	<crosshair id="2060002" path="circle.dds" /> <!-- Mind Shock -->
	<crosshair id="2020002" path="cross.dds" /> <!-- Gauss Rifle -->
	<crosshair id="2040003" path="stationary.dds" /> <!-- Senti Nell -->
	<crosshair id="2010006" path="cross.dds" /> <!-- Smash Rifle -->
	<crosshair id="2010007" path="cross.dds" /> <!-- Handgun -->
	<crosshair id="2010008" path="cross.dds" /> <!-- Shotgun -->
	<crosshair id="2010016" path="circle.dds" /> <!-- Air Gun -->
	<crosshair id="2010015" path="circle1.dds" /> <!-- Homing Rifle -->
	<crosshair id="2051337" path="circle.dds" /> <!-- Air Gun -->
	<crosshair id="2010019" path="circle1.dds" /> <!-- Shockwave Gun -->
	<crosshair id="2020007" path="circle1.dds" /> <!-- Lightmachine Gun -->
	<crosshair id="2010018" path="circle1.dds" /> <!-- Spark Rifle -->
	<crosshair id="2010024" path="cross.dds" /> <!-- Assault Rifle -->
	<crosshair id="2050004" path="projectile.dds" /> <!-- Rescue Gun -->
	<crosshair id="2030006"> <!-- Sharpshooter -->
		<primary path="cross.dds" />
		<secondary path="zoom.dds" />
	</crosshair>
	<crosshair id="2010028" path="cross.dds" /> <!-- Dual Magnum -->
	<crosshair id="2020005" path="cross.dds" /> <!-- Turret -->
</crosshairs>
"""

dom = minidom.parseString(restore)

with open('crosshairs.xml', 'w') as fich:
    dom.writexml(fich)