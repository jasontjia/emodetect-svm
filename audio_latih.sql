-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jun 07, 2024 at 01:43 PM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `audio`
--

-- --------------------------------------------------------

--
-- Table structure for table `audio_latih`
--

CREATE TABLE `audio_latih` (
  `id_audio_latih` int(11) NOT NULL,
  `nama_audio_latih` varchar(150) NOT NULL,
  `nada_ori_latih` varchar(150) NOT NULL,
  `intonasi_ori_latih` varchar(150) NOT NULL,
  `volume_ori_latih` varchar(150) NOT NULL,
  `label_manual_latih` varchar(150) NOT NULL,
  `label_otomatis_latih` varchar(150) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

--
-- Dumping data for table `audio_latih`
--

INSERT INTO `audio_latih` (`id_audio_latih`, `nama_audio_latih`, `nada_ori_latih`, `intonasi_ori_latih`, `volume_ori_latih`, `label_manual_latih`, `label_otomatis_latih`) VALUES
(611, 'ori_latih-marah120.wav', '1086.749', '4.897', '0.042', 'Marah', 'Marah'),
(612, 'ori_latih-tidakmarah1.wav', '1472.961', '3.514', '0.007', 'Tidak Marah', 'Tidak Marah'),
(621, 'ori_latih-tidakmarah3.wav', '1453.736', '3.516', '0.013', 'Tidak Marah', 'Tidak Marah'),
(622, 'ori_latih-tidakmarah4.wav', '1745.117', '3.678', '0.008', 'Tidak Marah', 'Tidak Marah'),
(623, 'ori_latih-tidakmarah5.wav', '1108.248', '4.275', '0.004', 'Tidak Marah', 'Tidak Marah'),
(624, 'ori_latih-tidakmarah6.wav', '2012.207', '3.548', '0.006', 'Tidak Marah', 'Tidak Marah'),
(625, 'ori_latih-tidakmarah7.wav', '1346.047', '3.987', '0.003', 'Tidak Marah', 'Tidak Marah'),
(626, 'ori_latih-tidakmarah8.wav', '1704.994', '3.431', '0.008', 'Tidak Marah', 'Tidak Marah'),
(627, 'ori_latih-tidakmarah9.wav', '1757.145', '3.496', '0.011', 'Tidak Marah', 'Tidak Marah'),
(628, 'ori_latih-tidakmarah10.wav', '1384.537', '3.596', '0.017', 'Tidak Marah', 'Tidak Marah'),
(629, 'ori_latih-tidakmarah11.wav', '1836.151', '3.425', '0.011', 'Tidak Marah', 'Tidak Marah'),
(630, 'ori_latih-tidakmarah12.wav', '1171.879', '4.638', '0.005', 'Tidak Marah', 'Tidak Marah'),
(631, 'ori_latih-tidakmarah13.wav', '2064.97', '3.506', '0.009', 'Tidak Marah', 'Tidak Marah'),
(632, 'ori_latih-tidakmarah14.wav', '1402.109', '3.666', '0.006', 'Tidak Marah', 'Tidak Marah'),
(633, 'ori_latih-tidakmarah15.wav', '1683.691', '3.42', '0.006', 'Tidak Marah', 'Tidak Marah'),
(634, 'ori_latih-tidakmarah16.wav', '1699.313', '3.614', '0.012', 'Tidak Marah', 'Tidak Marah'),
(635, 'ori_latih-tidakmarah17.wav', '1677.411', '3.566', '0.016', 'Tidak Marah', 'Tidak Marah'),
(636, 'ori_latih-tidakmarah18.wav', '1664.919', '3.47', '0.009', 'Tidak Marah', 'Tidak Marah'),
(637, 'ori_latih-tidakmarah19.wav', '709.412', '5.608', '0.004', 'Tidak Marah', 'Tidak Marah'),
(638, 'ori_latih-tidakmarah20.wav', '1879.624', '3.55', '0.006', 'Tidak Marah', 'Tidak Marah'),
(639, 'ori_latih-tidakmarah21.wav', '1540.782', '3.887', '0.007', 'Tidak Marah', 'Tidak Marah'),
(640, 'ori_latih-tidakmarah22.wav', '1476.695', '3.688', '0.006', 'Tidak Marah', 'Tidak Marah'),
(641, 'ori_latih-tidakmarah23.wav', '1654.87', '3.501', '0.012', 'Tidak Marah', 'Tidak Marah'),
(642, 'ori_latih-tidakmarah24.wav', '1276.611', '3.724', '0.011', 'Tidak Marah', 'Tidak Marah'),
(643, 'ori_latih-tidakmarah25.wav', '1670.258', '3.563', '0.012', 'Tidak Marah', 'Tidak Marah'),
(644, 'ori_latih-tidakmarah26.wav', '681.872', '5.039', '0.008', 'Tidak Marah', 'Tidak Marah'),
(645, 'ori_latih-tidakmarah27.wav', '1916.288', '3.579', '0.008', 'Tidak Marah', 'Tidak Marah'),
(646, 'ori_latih-tidakmarah28.wav', '1540.782', '3.887', '0.007', 'Tidak Marah', 'Tidak Marah'),
(647, 'ori_latih-tidakmarah29.wav', '1746.086', '3.411', '0.011', 'Tidak Marah', 'Tidak Marah'),
(648, 'ori_latih-tidakmarah30.wav', '1846.791', '3.606', '0.031', 'Tidak Marah', 'Tidak Marah'),
(649, 'ori_latih-tidakmarah31.wav', '1478.165', '3.511', '0.037', 'Tidak Marah', 'Tidak Marah'),
(650, 'ori_latih-tidakmarah32.wav', '1843.916', '3.474', '0.024', 'Tidak Marah', 'Tidak Marah'),
(651, 'ori_latih-tidakmarah33.wav', '965.987', '4.654', '0.006', 'Tidak Marah', 'Marah'),
(652, 'ori_latih-tidakmarah34.wav', '1986.859', '3.539', '0.046', 'Tidak Marah', 'Tidak Marah'),
(653, 'ori_latih-tidakmarah35.wav', '1518.125', '3.932', '0.024', 'Tidak Marah', 'Tidak Marah'),
(654, 'ori_latih-tidakmarah36.wav', '1615.667', '3.48', '0.014', 'Tidak Marah', 'Tidak Marah'),
(655, 'ori_latih-tidakmarah37.wav', '1873.681', '3.516', '0.032', 'Tidak Marah', 'Tidak Marah'),
(656, 'ori_latih-tidakmarah38.wav', '1327.798', '3.54', '0.057', 'Tidak Marah', 'Tidak Marah'),
(657, 'ori_latih-tidakmarah39.wav', '1732.896', '3.641', '0.031', 'Tidak Marah', 'Tidak Marah'),
(658, 'ori_latih-tidakmarah40.wav', '1222.967', '4.48', '0.014', 'Tidak Marah', 'Tidak Marah'),
(659, 'ori_latih-tidakmarah41.wav', '1974.525', '3.497', '0.041', 'Tidak Marah', 'Tidak Marah'),
(660, 'ori_latih-tidakmarah42.wav', '1991.24', '3.643', '0.028', 'Tidak Marah', 'Tidak Marah'),
(661, 'ori_latih-tidakmarah43.wav', '1557.741', '3.483', '0.018', 'Tidak Marah', 'Tidak Marah'),
(662, 'ori_latih-tidakmarah44.wav', '1785.511', '3.468', '0.021', 'Tidak Marah', 'Tidak Marah'),
(663, 'ori_latih-tidakmarah45.wav', '1168.265', '4.075', '0.068', 'Tidak Marah', 'Tidak Marah'),
(669, 'ori_latih-tidakmarah46.wav', '1849.52', '3.61', '0.027', 'Tidak Marah', 'Tidak Marah'),
(670, 'ori_latih-tidakmarah47.wav', '805.289', '4.489', '0.013', 'Tidak Marah', 'Tidak Marah'),
(671, 'ori_latih-tidakmarah48.wav', '1999.659', '3.818', '0.041', 'Tidak Marah', 'Tidak Marah'),
(672, 'ori_latih-tidakmarah49.wav', '1610.34', '3.825', '0.02', 'Tidak Marah', 'Tidak Marah'),
(673, 'ori_latih-tidakmarah50.wav', '1647.651', '3.436', '0.016', 'Tidak Marah', 'Tidak Marah'),
(674, 'ori_latih-tidakmarah51.wav', '1791.174', '3.679', '0.023', 'Tidak Marah', 'Tidak Marah'),
(675, 'ori_latih-tidakmarah52.wav', '1311.209', '3.841', '0.038', 'Tidak Marah', 'Tidak Marah'),
(676, 'ori_latih-tidakmarah53.wav', '1715.479', '3.447', '0.041', 'Tidak Marah', 'Tidak Marah'),
(677, 'ori_latih-tidakmarah54.wav', '847.818', '5.455', '0.013', 'Tidak Marah', 'Tidak Marah'),
(678, 'ori_latih-tidakmarah55.wav', '1866.859', '3.826', '0.049', 'Tidak Marah', 'Tidak Marah'),
(679, 'ori_latih-tidakmarah2.wav', '1800.742', '3.415', '0.013', 'Tidak Marah', 'Tidak Marah'),
(680, 'ori_latih-tidakmarah56.wav', '1574.198', '4.331', '0.035', 'Tidak Marah', 'Tidak Marah'),
(681, 'ori_latih-tidakmarah57.wav', '1025.617', '5.262', '0.008', 'Tidak Marah', 'Tidak Marah'),
(682, 'ori_latih-tidakmarah58.wav', '1209.409', '4.686', '0.006', 'Tidak Marah', 'Tidak Marah'),
(683, 'ori_latih-tidakmarah59.wav', '1470.722', '5.244', '0.006', 'Tidak Marah', 'Tidak Marah'),
(684, 'ori_latih-tidakmarah60.wav', '687.575', '5.679', '0.007', 'Tidak Marah', 'Tidak Marah'),
(767, 'ori_latih-tidakmarah61.wav', '1694.629', '4.048', '0.015', 'Tidak Marah', 'Tidak Marah'),
(768, 'ori_latih-tidakmarah62.wav', '1518.103', '4.403', '0.018', 'Tidak Marah', 'Tidak Marah'),
(769, 'ori_latih-tidakmarah63.wav', '1718.224', '4.54', '0.017', 'Tidak Marah', 'Tidak Marah'),
(770, 'ori_latih-tidakmarah64.wav', '1463.153', '4.889', '0.019', 'Tidak Marah', 'Tidak Marah'),
(777, 'ori_latih-tidakmarah71.wav', '1247.799', '3.751', '0.026', 'Tidak Marah', 'Tidak Marah'),
(778, 'ori_latih-tidakmarah72.wav', '1443.284', '4.085', '0.037', 'Tidak Marah', 'Tidak Marah'),
(779, 'ori_latih-marah61.wav', '926.793', '5.785', '0.038', 'Marah', 'Marah'),
(780, 'ori_latih-marah62.wav', '1781.17', '3.384', '0.015', 'Marah', 'Marah'),
(781, 'ori_latih-marah63.wav', '1527.725', '3.769', '0.012', 'Marah', 'Tidak Marah'),
(782, 'ori_latih-marah64.wav', '1646.015', '3.444', '0.004', 'Marah', 'Marah'),
(783, 'ori_latih-marah65.wav', '1622.835', '3.553', '0.014', 'Marah', 'Marah'),
(784, 'ori_latih-marah66.wav', '1381.878', '3.984', '0.018', 'Marah', 'Tidak Marah'),
(785, 'ori_latih-marah67.wav', '1948.253', '3.476', '0.006', 'Marah', 'Marah'),
(786, 'ori_latih-marah68.wav', '1888.796', '3.923', '0.021', 'Marah', 'Marah'),
(787, 'ori_latih-marah69.wav', '1775.451', '3.43', '0.016', 'Marah', 'Marah'),
(788, 'ori_latih-marah70.wav', '1678.624', '3.463', '0.013', 'Marah', 'Tidak Marah'),
(789, 'ori_latih-marah71.wav', '1771.833', '3.379', '0.016', 'Marah', 'Marah'),
(790, 'ori_latih-marah72.wav', '1653.825', '3.604', '0.018', 'Marah', 'Tidak Marah'),
(796, 'ori_latih-tidakmarah65.wav', '1246.606', '4.016', '0.026', 'Tidak Marah', 'Tidak Marah'),
(797, 'ori_latih-tidakmarah66.wav', '1179.902', '4.027', '0.003', 'Tidak Marah', 'Tidak Marah'),
(799, 'ori_latih-tidakmarah68.wav', '1295.994', '3.89', '0.003', 'Tidak Marah', 'Tidak Marah'),
(800, 'ori_latih-tidakmarah69.wav', '1445.261', '3.555', '0.005', 'Tidak Marah', 'Tidak Marah'),
(801, 'ori_latih-tidakmarah70.wav', '1469.049', '3.832', '0.033', 'Tidak Marah', 'Tidak Marah'),
(802, 'ori_latih-tidakmarah73.wav', '1824.956', '3.765', '0.027', 'Tidak Marah', 'Tidak Marah'),
(803, 'ori_latih-tidakmarah74.wav', '1658.11', '3.657', '0.029', 'Tidak Marah', 'Tidak Marah'),
(804, 'ori_latih-tidakmarah75.wav', '1841.484', '3.476', '0.097', 'Tidak Marah', 'Tidak Marah'),
(805, 'ori_latih-tidakmarah76.wav', '1789.806', '3.871', '0.092', 'Tidak Marah', 'Tidak Marah'),
(806, 'ori_latih-tidakmarah77.wav', '1832.019', '3.521', '0.123', 'Tidak Marah', 'Tidak Marah'),
(809, 'ori_latih-tidakmarah80.wav', '1391.91', '3.93', '0.03', 'Tidak Marah', 'Tidak Marah'),
(810, 'ori_latih-tidakmarah88.wav', '451.217', '7.362', '0.025', 'Tidak Marah', 'Tidak Marah'),
(811, 'ori_latih-tidakmarah87.wav', '1000.089', '4.584', '0.027', 'Tidak Marah', 'Tidak Marah'),
(812, 'ori_latih-tidakmarah86.wav', '1025.636', '5.709', '0.029', 'Tidak Marah', 'Tidak Marah'),
(814, 'ori_latih-tidakmarah84.wav', '451.581', '7.772', '0.007', 'Tidak Marah', 'Tidak Marah'),
(815, 'ori_latih-tidakmarah83.wav', '527.24', '9.187', '0.006', 'Tidak Marah', 'Tidak Marah'),
(816, 'ori_latih-tidakmarah82.wav', '726.076', '7.08', '0.006', 'Tidak Marah', 'Tidak Marah'),
(817, 'ori_latih-tidakmarah81.wav', '818.03', '6.099', '0.006', 'Tidak Marah', 'Tidak Marah'),
(819, 'ori_latih-marah74.wav', '1768.605', '3.702', '0.007', 'Marah', 'Marah'),
(820, 'ori_latih-tidakmarah2.wav', '1800.742', '3.415', '0.013', 'Tidak Marah', 'Tidak Marah'),
(826, 'ori_latih-marah119.wav', '1898.934', '3.928', '0.096', 'Marah', 'Marah'),
(827, 'ori_latih-marah118.wav', '1778.327', '3.609', '0.088', 'Marah', 'Marah'),
(829, 'ori_latih-marah116.wav', '1761.591', '3.461', '0.045', 'Marah', 'Marah'),
(830, 'ori_latih-marah115.wav', '1495.789', '3.563', '0.104', 'Marah', 'Marah'),
(833, 'ori_latih-marah112.wav', '1785.344', '3.966', '0.12', 'Marah', 'Marah'),
(849, 'ori_latih-marah117.wav', '1489.661', '4.209', '0.11', 'Marah', 'Marah'),
(861, 'ori_latih-marah107.wav', '1638.898', '3.501', '0.08', 'Marah', 'Marah'),
(864, 'ori_latih-marah61.wav', '926.793', '5.785', '0.038', 'Marah', 'Marah'),
(865, 'ori_latih-marah62.wav', '1781.17', '3.384', '0.015', 'Marah', 'Marah'),
(867, 'ori_latih-marah64.wav', '1646.015', '3.444', '0.004', 'Marah', 'Marah'),
(868, 'ori_latih-marah65.wav', '1622.835', '3.553', '0.014', 'Marah', 'Marah'),
(870, 'ori_latih-marah67.wav', '1948.253', '3.476', '0.006', 'Marah', 'Marah'),
(871, 'ori_latih-marah67.wav', '1948.253', '3.476', '0.006', 'Marah', 'Marah'),
(872, 'ori_latih-marah68.wav', '1888.796', '3.923', '0.021', 'Marah', 'Marah'),
(873, 'ori_latih-marah69.wav', '1775.451', '3.43', '0.016', 'Marah', 'Marah'),
(875, 'ori_latih-marah71.wav', '1771.833', '3.379', '0.016', 'Marah', 'Marah'),
(889, 'ori_latih-marah63.wav', '1527.725', '3.769', '0.012', 'Marah', 'Tidak Marah'),
(891, 'ori_latih-marah101.wav', '1655.686', '3.635', '0.05', 'Marah', 'Tidak Marah'),
(893, 'ori_latih-marah108.wav', '1408.991', '3.786', '0.079', 'Marah', 'Tidak Marah'),
(894, 'ori_latih-marah109.wav', '1803.051', '3.465', '0.072', 'Marah', 'Tidak Marah'),
(895, 'ori_latih-marah110.wav', '1390.024', '4.08', '0.109', 'Marah', 'Tidak Marah');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `audio_latih`
--
ALTER TABLE `audio_latih`
  ADD PRIMARY KEY (`id_audio_latih`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `audio_latih`
--
ALTER TABLE `audio_latih`
  MODIFY `id_audio_latih` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=899;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
